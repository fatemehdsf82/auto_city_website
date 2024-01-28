from django import forms


class AddToFavoriteProductForm(forms.Form):
    QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 31)]

    quantity = forms.TypedChoiceField(coerce=int, choices=QUANTITY_CHOICES)
    inplace = forms.BooleanField(required=False, widget=forms.HiddenInput)
