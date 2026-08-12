import json
import logging
from smtplib import SMTPException

import requests
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.core.mail import BadHeaderError, EmailMultiAlternatives, send_mail
from django.db import DatabaseError, IntegrityError
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import TemplateDoesNotExist
from django.template.loader import render_to_string
from django.urls import NoReverseMatch, reverse
from django.utils import timezone
from django.views.decorators.http import require_POST

# If you are using django-ratelimit:
from accounts.forms import UserRegisterForm

from .decorators import admin_only, unauthenticated_user
from .models import Profile


def verify_turnstile(token, remote_ip=None):
    response = requests.post(
        "https://challenges.cloudflare.com/turnstile/v0/siteverify",
        data={
            "secret": settings.TURNSTILE_SECRET_KEY,
            "response": token,
            "remoteip": remote_ip,
        },
        timeout=10,
    )

    result = response.json()

    return result.get("success", False)


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")

    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0].strip()
    else:
        ip = request.META.get("REMOTE_ADDR")

    return ip


def account_access_denied(request):
    reason = request.GET.get("reason")
    return render(request, "accounts/account_access_denied.html", {"reason": reason})


User = get_user_model()


logger = logging.getLogger(__name__)


@unauthenticated_user
# @ratelimit(key="user_or_ip", rate="5/h", block=True)
def register(request: HttpRequest) -> HttpResponse:

    if request.method == "POST":
        # --------------------------------------------------
        # 1. Create form
        # --------------------------------------------------
        form = UserRegisterForm(request.POST)

        # --------------------------------------------------
        # 2. Cloudflare Turnstile
        # --------------------------------------------------
        turnstile_token = request.POST.get("cf-turnstile-response")

        if not turnstile_token:
            messages.error(
                request,
                "Please complete the security verification.",
            )

            return render(
                request,
                "accounts/register.html",
                {
                    "form": form,
                    "TURNSTILE_SITE_KEY": settings.TURNSTILE_SITE_KEY,
                },
            )

        try:
            turnstile_valid = verify_turnstile(
                turnstile_token,
                request.META.get("REMOTE_ADDR"),
            )

        except Exception:
            logger.exception("Turnstile verification failed.")

            messages.error(
                request,
                "Security verification failed. Please try again.",
            )

            return render(
                request,
                "accounts/register.html",
                {
                    "form": form,
                    "TURNSTILE_SITE_KEY": settings.TURNSTILE_SITE_KEY,
                },
            )

        if not turnstile_valid:
            messages.error(
                request,
                "Please complete the security verification.",
            )

            return render(
                request,
                "accounts/register.html",
                {
                    "form": form,
                    "TURNSTILE_SITE_KEY": settings.TURNSTILE_SITE_KEY,
                },
            )

        # --------------------------------------------------
        # 3. Form validation
        # --------------------------------------------------
        if not form.is_valid():
            return render(
                request,
                "accounts/register.html",
                {
                    "form": form,
                    "TURNSTILE_SITE_KEY": settings.TURNSTILE_SITE_KEY,
                },
            )

        # --------------------------------------------------
        # 4. Create user
        # --------------------------------------------------
        try:
            user = form.save(commit=False)
            user.save()

        except IntegrityError:
            logger.exception("Database integrity error during registration.")

            messages.error(
                request,
                "An account with these details may already exist.",
            )

            return render(
                request,
                "accounts/register.html",
                {
                    "form": form,
                    "TURNSTILE_SITE_KEY": settings.TURNSTILE_SITE_KEY,
                },
            )

        except DatabaseError:
            logger.exception("Database error during registration.")

            messages.error(
                request,
                "We could not create your account. Please try again later.",
            )

            return render(
                request,
                "accounts/register.html",
                {
                    "form": form,
                    "TURNSTILE_SITE_KEY": settings.TURNSTILE_SITE_KEY,
                },
            )

        except Exception:
            logger.exception("Unexpected error while creating user.")

            messages.error(
                request,
                "We could not create your account. Please try again later.",
            )

            return render(
                request,
                "accounts/register.html",
                {
                    "form": form,
                    "TURNSTILE_SITE_KEY": settings.TURNSTILE_SITE_KEY,
                },
            )

        # --------------------------------------------------
        # 5. Build login URL
        # --------------------------------------------------
        try:
            login_url = request.build_absolute_uri(reverse("login"))

        except NoReverseMatch:
            logger.exception("Could not reverse the login URL.")

            # Account has already been created, so don't
            # show a server error to the user.
            messages.warning(
                request,
                "Account created, but we could not generate the login link. "
                "Please contact support.",
            )

            return redirect("login")

        # --------------------------------------------------
        # 6. Send emails
        # --------------------------------------------------
        try:
            # ----------------------------------------------
            # User registration email
            # ----------------------------------------------
            user_html = render_to_string(
                "emails/user_registration.html",
                {
                    "user": user,
                    "login_url": login_url,
                },
            )

            user_email = EmailMultiAlternatives(
                subject="Welcome to Octo - Account Created",
                body=(
                    "Welcome to Octo.\n\n"
                    f"Login ID: {user.username}\n"
                    f"Login URL: {login_url}\n\n"
                    "Your account has been created successfully. "
                    "You can now log in using the password you chose during registration."
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[user.email],
            )

            user_email.attach_alternative(
                user_html,
                "text/html",
            )

            user_email.send(fail_silently=False)

            # ----------------------------------------------
            # Admin registration email
            # ----------------------------------------------
            admin_html = render_to_string(
                "emails/admin_new_registration.html",
                {
                    "user": user,
                    "registered_on": timezone.now(),
                    "admin_url": request.build_absolute_uri("/admin/"),
                },
            )

            admin_email = EmailMultiAlternatives(
                subject="New User Registration - Approval Required",
                body=(
                    "New user registered on Saznara.\n\n"
                    f"Username: {user.username}\n"
                    f"Email: {user.email}\n"
                    f"Name: {user.get_full_name()}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.ADMIN_EMAIL],
            )

            admin_email.attach_alternative(
                admin_html,
                "text/html",
            )

            admin_email.send(fail_silently=False)

            # ----------------------------------------------
            # Success
            # ----------------------------------------------
            messages.success(
                request,
                "Account created successfully. You can now log in.",
            )

        except (
            BadHeaderError,
            TemplateDoesNotExist,
            OSError,
        ) as e:
            logger.exception(
                "Registration email/template error: %s",
                e,
            )

            messages.warning(
                request,
                "Account created, but we could not send the email. "
                "Please contact support.",
            )

        except Exception as e:
            logger.exception(
                "Unexpected registration email error: %s",
                e,
            )

            messages.warning(
                request,
                "Account created, but email delivery failed. Please contact support.",
            )

        # --------------------------------------------------
        # 7. Redirect after successful registration
        # --------------------------------------------------
        return redirect("login")

    # ------------------------------------------------------
    # GET request
    # ------------------------------------------------------
    form = UserRegisterForm()

    return render(
        request,
        "accounts/register.html",
        {
            "form": form,
            "TURNSTILE_SITE_KEY": settings.TURNSTILE_SITE_KEY,
        },
    )


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        import logging

        logger = logging.getLogger(__name__)

        logger.warning("LOGIN USERNAME RECEIVED: %r", username)
        logger.warning(
            "LOGIN PASSWORD RECEIVED LENGTH: %s", len(password) if password else None
        )

        user = authenticate(request, username=username, password=password)

        logger.warning("AUTH RESULT: %r", user)

        if user is not None:
            # 🔴 Admin bypass (no profile needed)
            is_admin = user.is_superuser or user.groups.filter(name="Admin").exists()

            if not is_admin:
                try:
                    profile = user.profile
                except Profile.DoesNotExist:
                    messages.error(request, "Profile not found.")
                    return render(request, "accounts/login.html")

                # ❌ Block inactive
                if not profile.is_active:
                    messages.error(request, "Account is inactive.")
                    return redirect("/accounts/account-access-denied/?reason=inactive")

                # ❌ Block not approved
                if not profile.is_approved:
                    messages.error(request, "Account not approved.")
                    return redirect("/accounts/account-access-denied/?reason=approval")

            # ✅ LOGIN only after all checks pass
            login(request, user)
            return redirect("/")

        messages.error(request, "Invalid credentials.")

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect("login")


@login_required
def dashboard(request):

    if request.user.is_superuser or request.user.groups.filter(name="Admin").exists():
        return render(request, "accounts/dashboard.html")

    profile = getattr(request.user, "profile", None)

    if not profile:
        messages.warning(request, "Please complete your profile.")
        return redirect("update_profile")

    if not profile.address:
        messages.warning(
            request, "Please update your profile before accessing dashboard."
        )
        return redirect("update_profile")

    if not profile.is_approved:
        messages.error(request, "Your account is not approved.")
        return redirect("not_approved")

    return render(request, "accounts/dashboard.html")


@login_required
def view_profile(request, id):

    profile = get_object_or_404(Profile, id=id)

    if not (request.user == profile.user or request.user.is_superuser):
        return redirect("Not_Authorised")

    return render(request, "accounts/user-profile.html", {"profile": profile})


@login_required
def update_profile(request, id):
    profile = get_object_or_404(Profile, id=id, user=request.user)

    if not profile.is_profile_complete:
        messages.warning(request, "Please complete your profile before continuing.")

    if request.method == "POST":
        profile.user.email = request.POST.get("email")
        profile.user.save()

        profile.company = request.POST.get("company")
        profile.mobile_no = request.POST.get("mobile_no")
        profile.pin = request.POST.get("pin")
        profile.address = request.POST.get("address")

        if request.FILES.get("image"):
            profile.image = request.FILES["image"]

        profile.save()

        messages.success(request, "Profile updated successfully.")
        return redirect("user-profile", id=profile.id)

    return render(
        request,
        "accounts/edit-profile.html",
        {
            "profile": profile,
        },
    )


def send_email(request):
    if request.method == "POST":
        message = request.POST.get("message")
        recipient = "sandeep0782@gmail.com"  # Change to your recipient email
        try:
            send_mail(
                "New Message from Profile Card",
                message,
                "myfabricae@gmail.com",  # Your email
                [recipient],
                fail_silently=False,
            )
            messages.success(request, "Email sent successfully!")
        except BadHeaderError:
            messages.error(request, "Invalid email header detected.")

        except SMTPException as e:
            messages.error(request, f"Email sending failed: {e}")
    return render(request, "profile_not_approved.html")


@login_required
def Not_Authorised(request):
    return render(request, "401.html")


@login_required
@admin_only
@require_POST
def Is_Active(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"success": False, "error": "Invalid JSON"}, status=400)

        item_id = data.get("id")
        is_active = data.get("is_active")

        try:
            item = Profile.objects.get(id=item_id)
            item.is_active = is_active
            item.save()
            return JsonResponse({"success": True})
        except Profile.DoesNotExist:
            return JsonResponse(
                {"success": False, "error": "Item not found"}, status=404
            )

    return JsonResponse({"success": False, "error": "Invalid request"}, status=400)


@login_required
@admin_only
@require_POST
def Is_Approved(request):
    if request.method == "POST":
        data = json.loads(request.body)
        item_id = data.get("id")
        is_approved = data.get("is_approved")

        try:
            item = Profile.objects.get(id=item_id)
            item.is_approved = is_approved
            item.save()
            return JsonResponse({"success": True})
        except Profile.DoesNotExist:
            return JsonResponse(
                {"success": False, "error": "Item not found"}, status=404
            )

    return JsonResponse({"success": False, "error": "Invalid request"}, status=400)


class CustomPasswordResetView(PasswordResetView):
    def send_mail(
        self,
        subject_template_name,
        email_template_name,
        context,
        from_email,
        to_email,
        html_email_template_name=None,
    ):

        subject = render_to_string(subject_template_name, context)

        subject = "".join(subject.splitlines())

        # Plain text version
        text_content = render_to_string("accounts/password_reset_email.txt", context)

        # HTML version
        html_content = render_to_string("accounts/password_reset_email.html", context)

        email = EmailMultiAlternatives(
            subject,
            text_content,  # IMPORTANT: txt file here
            settings.DEFAULT_FROM_EMAIL,
            [to_email],
        )

        email.attach_alternative(html_content, "text/html")

        email.send()
