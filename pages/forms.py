from django import forms


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
