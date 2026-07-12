from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from accounts.forms import UserRegisterForm
from django.core.mail import send_mail
from django.contrib.auth import logout
from django.http import HttpResponse
from .forms import ProfileUpdateForm
from django.contrib import messages
from .models import USER_ROLE, Profile
import json

def account_access_denied(request):
    reason = request.GET.get('reason')
    return render(request, 'accounts/account_access_denied.html', {'reason': reason})

# Create your views here.
@unauthenticated_user
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile


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


from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileUpdateForm

@login_required
def Change_Vendor(request, id=None):
    vendor = None
    if id:
        try:
            vendor = Profile.objects.get(id=id)
        except ObjectDoesNotExist:
            messages.error(request, "Vendor profile not found.")
            return redirect('view_vendor')  # Redirect to a default page if the vendor is not found
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        form1 = ProfileUpdateForm(request.POST)
        
        if form.is_valid() and form1.is_valid():
            user = form.save()
            # Now create the vendor profile associated with the user
            profile = form1.save(commit=False)  # Don't save yet
            profile.user = user  # Associate the user with the profile
            profile.save()  # Save the profile
            
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')  # Redirect to login after account creation
        
        # Handle form errors
        else:
            messages.error(request, 'Please correct the errors below.')

    else:
        form = UserRegisterForm()
        form1 = ProfileUpdateForm()

    user_role = USER_ROLE  # Ensure this is defined properly elsewhere

    return render(request, 'accounts/vendor/change_vendor.html', {
        'form': form,
        'form1': form1,
        'user_role': user_role,
        'vendor': vendor,  # Pass the vendor profile if it's being edited
    })



@login_required
def dashboard(request):
    # Check if the profile is incomplete
    if not request.user.profile.address:
        messages.warning(request, "Please update your profile before accessing the dashboard.")
        return redirect('update_profile')

    # Check if the user is approved by the admin
    if not request.user.profile.is_approved:
        messages.error(request, "Your account is not approved by the admin yet.")
        return redirect('not_approved')

    return render(request, 'accounts/dashboard.html')

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('dashboard')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'accounts/user-profile.html', {'form': form})


# views.py


# @csrf_exempt
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
        except:
            pass
    return render(request, 'profile_not_approved.html')
    
def Not_Authorised(request):
    return render(request, '401.html')



from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Only if you're handling the CSRF token manually in the JS
def Is_Active(request):
    if request.method == "POST":
        data = json.loads(request.body)
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


@csrf_exempt  # Only if you're handling the CSRF token manually in the JS
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