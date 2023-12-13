# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm


# class SignUpForm(UserCreationForm):
#     class Meta:
#         model=User
#         fields = ['username','email','password1','password2']


# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


# class SignUpForm(UserCreationForm):
#     email = forms.EmailField(
#         max_length=254, help_text="Required. Enter a valid email address."
#     )

#     class Meta:
#         model = User
#         fields: list[str] = ["username", "email", "password1", "password2"]


# from dataclasses import fields
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.contrib.auth import get_user_model


# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = get_user_model()
#         fields = ("email", "username")


# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = get_user_model()
#         fields = ("email", "username")
