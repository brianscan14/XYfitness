from django import forms
from .models import Review


class PostReviewForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-textfield',
            'rows': '8',
            'placeholder': 'Enter your experience with XY fitness here..'
        }),
        min_length=40
    )

    class Meta:
        model = Review
        fields = (
            'title', 'content', 'before_picture', 'after_picture'
        )
