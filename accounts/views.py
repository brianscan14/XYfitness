from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth import update_session_auth_hash
from accounts.forms import (
    UserLoginForm, UserRegistrationForm, ProfileUpdateForm, ProfilePic
)
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .models import Profile


@login_required
def logout(request):
    """logs user out and returns to home page"""
    auth.logout(request)
    messages.success(request, "Successfully logged out")
    return redirect(reverse('home'))


def login(request):
    """
    If user is already logged in a message is displayed telling
    them this. If they fill in their details correctly they will
    be logged in, else the errors returned. If the user tried to
    access a page that requires loggin in then they will be directed
    to that 'next' page, else returned to home.
    """
    if request.user.is_authenticated:
        messages.success(request, "Already logged in!")
        return redirect(reverse('home'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(
                username=request.POST['username'],
                password=request.POST['password']
            )
            messages.success(request, "You have successfully logged in!")

            if user:
                auth.login(user=user, request=request)
                return redirect(request.GET.get('next', 'home'))
            else:
                login_form.add_error(None, "Username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def register(request):
    """
    Renders the registration page, if the user somehow gets here
    when they are already logged in they are returned to home page
    with a message. Id there are issues with the form then the errors
    are returned. Upon successful registration the user's profile will
    also be created, taking from the register form, and the user directed
    to the home page.
    """
    if request.user.is_authenticated:
        messages.success(request, "Sure you're already registered! :)")
        return redirect(reverse('home'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST, request.FILES)

        if registration_form.is_valid():
            registration_form.save()
            user = auth.authenticate(
                username=request.POST['username'],
                password=request.POST['password1']
            )
            user.profile_pic = request.FILES['profile_pic']
            Profile.objects.create(
                user=user,
                username=request.POST['username'],
                profile_pic=request.FILES['profile_pic']
            )
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('home'))
            else:
                messages.error(request, "Unable to register your account")
    else:
        registration_form = UserRegistrationForm()

    return render(request, 'register.html', {
        "registration_form": registration_form
    })


@login_required
def profile(request):
    """Directs user to their profile page."""
    return render(request, 'profile.html')


@login_required
def update_profile(request):
    """Updates details of the user."""
    if request.method == 'POST':
        form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user
        )
        if form.is_valid():
            form.save()
            messages.success(request, f'Account updated.')
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'update.html', {"form": form})


@login_required
def update_profile_pic(request):
    """Updates profile picture of the user."""
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, f'Profile picture updated.')
            return redirect('profile')
    else:
        form = ProfilePic(instance=request.user)
    return render(request, 'profilepic.html', {"form": form})


@login_required
def update_password(request):
    """Updates password of the user using Django form."""
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Error, please correct')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password.html', {'form': form})
