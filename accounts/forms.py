from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]

    def clean_email(self):
        email = self.cleaned_data["email"].strip()

        if email.startswith("[") and "](" in email:
            email = email.split("](")[0].replace("[", "")

        return email

    def clean_username(self):
        username = self.cleaned_data["username"].strip()

        if username.startswith("[") and "](" in username:
            username = username.split("](")[0].replace("[", "")

        return username


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

    user_role = forms.ChoiceField(choices=USER_ROLE, required=True, widget=forms.Select)
