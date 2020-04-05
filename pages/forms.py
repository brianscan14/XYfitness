from django import forms


class EmailContactForm(forms.Form):
    email = forms.EmailField(required=True)
    title = forms.CharField(required=True, min_length=5, max_length=40)
    message = forms.CharField(widget=forms.Textarea(
        attrs={
            'rows': '9',
            'placeholder': 'We will reply as soon as we can :)'
        }),
        min_length=40, max_length=400, required=True)
