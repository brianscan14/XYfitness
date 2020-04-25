from django import forms
from .models import Review


class PostReviewForm(forms.ModelForm):
    """
    Fields used for the form a user fills out to add a testimonial.
    Attributes modified to ensure a better filled out testimonial.
    """
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Your Testimonial Title'
        }),
        min_length=5
    )
    content = forms.CharField(widget=forms.Textarea(
        attrs={
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
