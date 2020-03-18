from django import forms


class EmailContactForm(forms.Form):
    email = forms.EmailField(required=True)
    title = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
