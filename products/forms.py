from django import forms
from .models import ProductReview, Product


class ProdReviewForm(forms.ModelForm):

    class Meta:
        model = ProductReview
        fields = ('title', 'content', 'rating')


class ProdSizeForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
