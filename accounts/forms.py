from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Profile


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput
    )
    profile_pic = forms.ImageField(label='Profile Pic')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'profile_pic']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError(u'Email address must be included.')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Password must not be empty")

        if password1 != password2:
            raise ValidationError("Passwords do not match")

        return password2


class ProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    username = forms.CharField()
    profile_pic = forms.ImageField(label='Profile Pic')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'profile_pic']


class ProfilePic(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['profile_pic']
