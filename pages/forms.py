from tkinter import Widget
from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class ProductSearchForm(forms.Form):
    deposit_min = forms.IntegerField(required=False)
    deposit_max = forms.IntegerField(required=False)
    rent_min = forms.FloatField(required=False)
    rent_max = forms.FloatField(required=False)
    area_min = forms.IntegerField(required=False)
    DISTRICT_CHOICES = [(str(i), str(i)) for i in range(1, 23)]
    district = forms.TypedChoiceField(
        choices=DISTRICT_CHOICES, required=False, coerce=int, empty_value=None
    )


class ProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Profile
        fields = ["name", "family_name", "address", "phone_number", "email"]
        Widget = {
            "address": forms.Textarea(attrs={"rows": 3}),
            "email": forms.Textarea(
                attrs={
                    "rows": 1,
                    "placeholder": _("please enter the email you registered with it."),
                }
            ),
        }


# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ["name", "family_name", "address", "phone_number"]


# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ["name", "family_name", "address", "phone_number", "email"]

# def __init__(self, *args, **kwargs):
#     # ایجاد یک پارامتر initial برای فیلد email
#     initial_email = kwargs.get("initial", {}).get("email", "")
#     kwargs["initial"] = {"email": initial_email}
#     super().__init__(*args, **kwargs)

# def save(self, commit=True):
#     user = super().save(commit=False)
#     user.email = self.cleaned_data["email"]
#     if commit:
#         user.save()
#     return user
