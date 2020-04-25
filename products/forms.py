from django import forms
from .models import ProductReview


class ProdReviewForm(forms.ModelForm):
    """
    Fields for the form used in order to add a
    review for an item in the shop, rating is a
    dropdown selection of 1-5.
    """
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Add Review'
        }),
        min_length=5
    )
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'rows': '9',
            'placeholder': 'Please tell us what you think..'
        }),
        min_length=20
    )

    class Meta:
        model = ProductReview
        fields = ('title', 'content', 'rating')
