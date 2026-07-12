from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from . models import *


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email', 'password1', 'password2']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        
    user_role = forms.ChoiceField(choices=USER_ROLE, required=True, widget=forms.Select)

