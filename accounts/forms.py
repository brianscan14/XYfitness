from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Profile


# below code taken initially from a Code Institute tutorial when
# setting up and modified for my project
class UserLoginForm(forms.Form):
    """logs user in, password is hidden"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# below code taken initially from a Code Institute tutorial when
# setting up and modified for my project
class UserRegistrationForm(UserCreationForm):
    """reisters user and is used to create new profile"""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput
    )
    profile_pic = forms.ImageField(label='Profile Pic', required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'profile_pic']

    def clean_email(self):
        """
        checks for user of same address and raises error. Also
        ensure the fields have content in them.
        """
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError(u'Email address must be included.')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

    def clean_password2(self):
        """Compares passwords and raises error if they are not matching"""
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Password must not be empty")

        if password1 != password2:
            raise ValidationError("Passwords do not match")

        return password2


class ProfileUpdateForm(forms.ModelForm):
    """Form used to update some details about the user"""
    email = forms.EmailField()
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    username = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfilePic(forms.ModelForm):
    """Form used to update profile picture of user"""

    class Meta:
        model = Profile
        fields = ['profile_pic']
