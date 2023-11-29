from dataclasses import fields
from django import forms
from costumers.models import Costumer


class CostumersForm(forms.ModelForm):
    # first_name = forms.forms.CharField(max_length=50, name='first_name')
    # last_name = forms.forms.CharField(max_length=50, name='last_name')
    class Meta:
        model = Costumer
        fields = '__all__'