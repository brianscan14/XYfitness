from django import forms
from .models import Review


class PostReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = (
            'title', 'content', 'before_picture', 'after_picture'
        )
