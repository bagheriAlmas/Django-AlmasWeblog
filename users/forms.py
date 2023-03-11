from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username','password1','password2', 'email', 'instagram', 'twitter', 'avatar', 'about_me']
        # fields = ['username', 'password1','password2', 'avatar',]


class CustomUserChangeForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username','password1','password2', 'email', 'instagram', 'twitter', 'avatar', 'about_me']

        # fields = ['first_name', 'last_name', 'username', 'email', 'instagram', 'twitter', 'avatar', 'about_me']
        # fields = ['username', 'password1','password2', 'avatar',]
