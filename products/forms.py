from django import forms
from .models import ProductReview, Product


class ProdReviewForm(forms.ModelForm):
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


class ProdSizeForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
