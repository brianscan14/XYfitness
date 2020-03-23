from django import forms
from .models import ProductReview


class ProdReviewForm(forms.ModelForm):

    class Meta:
        model = ProductReview
        fields = ('title', 'content')
