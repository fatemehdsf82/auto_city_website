from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text", "star"]


class ProductSearchForm(forms.Form):
    p_name = forms.CharField(label="product_name", max_length=255)
