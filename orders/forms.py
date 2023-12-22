from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["first_name", "last_name", "phone_number", "address", "order_note"]
        Widget = {
            "address": forms.Textarea(attrs={"rows": 3}),
            "order_notes": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": _(
                        "if you have any notes please enter here, otherwise leave it empty."
                    ),
                }
            ),
        }
