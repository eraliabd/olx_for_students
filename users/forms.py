from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = UserCreationForm.Meta.fields+('first_name', 'last_name', 'phone_number', 'address', 'gender', 'age')


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = User
        fields = UserChangeForm.Meta.fields


# class CustomUserLoginForm(forms.Form):
#     phone_number = forms.CharField(max_length=20)
#     password = forms.CharField(widget=forms.PasswordInput)
