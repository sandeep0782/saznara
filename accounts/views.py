from .decorators import unauthenticated_user, allowed_users, admin_only
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login
from accounts.forms import ProfileUpdateForm, UserRegisterForm
from django.core.mail import send_mail
from django.contrib.auth import logout
from django.http import JsonResponse
from django.contrib import messages
from .models import Profile
import json

from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings


def account_access_denied(request):
    reason = request.GET.get('reason')
    return render(request, 'accounts/account_access_denied.html', {'reason': reason})


# Create your views here.
# @unauthenticated_user
# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Account created successfully! You can now log in.')
#             return redirect('login')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'accounts/register.html', {'form': form})

from django.conf import settings
from django.core.mail import send_mail

from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string

from django.template.loader import render_to_string
from django.conf import settings
from django.urls import reverse
from django.utils import timezone

User = get_user_model()

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.crypto import get_random_string
from django.utils import timezone
from django.urls import reverse


@unauthenticated_user
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            # Create user with temporary password
            user = form.save(commit=False)

            temp_password = get_random_string(length=10)

            user.set_password(temp_password)
            user.save()

            login_url = request.build_absolute_uri(
                reverse('login')
            )

            try:
                # -------------------------
                # Email to User
                # -------------------------
                user_html = render_to_string(
                    "emails/user_registration.html",
                    {
                        "user": user,
                        "password": temp_password,
                        "login_url": login_url,
                    }
                )

                user_email = EmailMultiAlternatives(
                    subject="Welcome to Octo - Account Created",
                    body=(
                        f"Welcome to Octo.\n\n"
                        f"Login ID: {user.username}\n"
                        f"Temporary Password: {temp_password}\n\n"
                        f"Login URL: {login_url}\n\n"
                        "Please change your password after first login."
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[user.email],
                )

                user_email.attach_alternative(
                    user_html,
                    "text/html"
                )

                user_email.send()


                # -------------------------
                # Email to Admin
                # -------------------------
                admin_html = render_to_string(
                    "emails/admin_new_registration.html",
                    {
                        "user": user,
                        "registered_on": timezone.now(),
                        "admin_url": request.build_absolute_uri(
                            "/admin/"
                        ),
                    }
                )

                admin_email = EmailMultiAlternatives(
                    subject="New User Registration - Approval Required",
                    body=(
                        f"New user registered on Saznara.\n\n"
                        f"Username: {user.username}\n"
                        f"Email: {user.email}\n"
                        f"Name: {user.get_full_name()}"
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[settings.ADMIN_EMAIL],
                )

                admin_email.attach_alternative(
                    admin_html,
                    "text/html"
                )

                admin_email.send()


                messages.success(
                    request,
                    "Account created. Login details have been sent to your email."
                )

            except Exception as e:
                messages.warning(
                    request,
                    f"Account created, but email delivery failed: {e}"
                )

            return redirect("login")

    else:
        form = UserRegisterForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form}
    )


def login_view(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:

            # 🔴 Admin bypass (no profile needed)
            is_admin = (
                user.is_superuser or
                user.groups.filter(name='Admin').exists()
            )

            if not is_admin:
                try:
                    profile = user.profile
                except Profile.DoesNotExist:
                    messages.error(request, "Profile not found.")
                    return render(request, 'accounts/login.html')

                # ❌ Block inactive
                if not profile.is_active:
                    messages.error(request, "Account is inactive.")
                    return redirect('/accounts/account-access-denied/?reason=inactive')

                # ❌ Block not approved
                if not profile.is_approved:
                    messages.error(request, "Account not approved.")
                    return redirect('/accounts/account-access-denied/?reason=approval')

            # ✅ LOGIN only after all checks pass
            login(request, user)
            return redirect('/')

        messages.error(request, "Invalid credentials.")

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('login')

@login_required
def dashboard(request):

    if request.user.is_superuser or request.user.groups.filter(name='Admin').exists():
        return render(request, 'accounts/dashboard.html')

    profile = getattr(request.user, 'profile', None)

    if not profile:
        messages.warning(request, "Please complete your profile.")
        return redirect('update_profile')

    if not profile.address:
        messages.warning(request, "Please update your profile before accessing dashboard.")
        return redirect('update_profile')

    if not profile.is_approved:
        messages.error(request, "Your account is not approved.")
        return redirect('not_approved')

    return render(request, 'accounts/dashboard.html')


@login_required
def view_profile(request,id):

    profile=get_object_or_404(Profile,id=id)

    if not (
        request.user == profile.user or
        request.user.is_superuser
    ):
        return redirect('Not_Authorised')

    return render(
        request,
        'accounts/user-profile.html',
        {'profile':profile}
    )


@login_required
def update_profile(request, id):
    profile = get_object_or_404( Profile, id=id, user=request.user)

    if not profile.is_profile_complete:
        messages.warning(
            request,
            "Please complete your profile before continuing."
        )

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

    return render(request, "accounts/edit-profile.html", {
        "profile": profile,
    })

def send_email(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        recipient = 'sandeep0782@gmail.com'  # Change to your recipient email
        try:
            send_mail(
                'New Message from Profile Card',
                message,
                'myfabricae@gmail.com',  # Your email
                [recipient],
                fail_silently=False,
            )
            messages.success(request, 'Email sent successfully!')
        except Exception as e:
            messages.error(request, str(e))
    return render(request, 'profile_not_approved.html')

@login_required    
def Not_Authorised(request):
    return render(request, '401.html')

@login_required
@admin_only
@require_POST
def Is_Active(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON'},status=400)
        
        item_id = data.get('id')
        is_active = data.get('is_active')

        try:
            item = Profile.objects.get(id=item_id)
            item.is_active = is_active
            item.save()
            return JsonResponse({'success': True})
        except Profile.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Item not found'}, status=404)

    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)

@login_required
@admin_only
@require_POST
def Is_Approved(request):
    if request.method == "POST":
        data = json.loads(request.body)
        item_id = data.get('id')
        is_approved = data.get('is_approved')

        try:
            item = Profile.objects.get(id=item_id)
            item.is_approved = is_approved
            item.save()
            return JsonResponse({'success': True})
        except Profile.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Item not found'}, status=404)

    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)


from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.views import PasswordResetView
from django.template.loader import render_to_string

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

        subject = render_to_string(
            subject_template_name,
            context
        )

        subject = ''.join(subject.splitlines())

        # Plain text version
        text_content = render_to_string(
            "accounts/password_reset_email.txt",
            context
        )

        # HTML version
        html_content = render_to_string(
            "accounts/password_reset_email.html",
            context
        )

        email = EmailMultiAlternatives(
            subject,
            text_content,   # IMPORTANT: txt file here
            settings.DEFAULT_FROM_EMAIL,
            [to_email]
        )

        email.attach_alternative(
            html_content,
            "text/html"
        )

        email.send()