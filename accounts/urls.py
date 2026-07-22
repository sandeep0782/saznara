from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # path('profile/', views.user_profile, name='user-profile'),
    # path('update_profile/', views.update_profile, name='update_profile'),

    path('profile/<int:id>/', views.view_profile, name='user-profile'),
    path('profile/<int:id>/edit/', views.update_profile, name='edit-profile'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path(
        'password_reset/',
        views.CustomPasswordResetView.as_view(
            template_name='accounts/password_reset.html',
            email_template_name='accounts/password_reset_email.txt',
            subject_template_name='accounts/password_reset_subject.txt'
        ),
        name='password_reset'
    ),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
    path('send-email/', views.send_email, name='send_email'),
    path('not_authorised/', views.Not_Authorised, name='not_authorised'),
    path('is_active/', views.Is_Active, name='toggle_is_active'),
    path('is_approved/', views.Is_Approved, name='toggle_is_approved'),

    path('account-access-denied/', views.account_access_denied, name='account_access_denied'),



]