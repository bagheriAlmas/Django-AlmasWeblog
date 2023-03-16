from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import forms

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'email', 'avatar']
        # fields = ['username', 'password1','password2', 'avatar',]


class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'facebook', 'twitter', 'avatar', 'about_me']

        # fields = ['first_name', 'last_name', 'username', 'email', 'instagram', 'twitter', 'avatar', 'about_me']
        # fields = ['username', 'password1','password2', 'avatar',]
