from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth
from django.contrib.auth import update_session_auth_hash
from accounts.forms import (
    UserLoginForm, UserRegistrationForm, ProfileUpdateForm, ProfilePic
)
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .models import Profile
import sweetify


@login_required
def logout(request):
    """logs user out and returns to home page"""
    auth.logout(request)
    sweetify.success(
        request,
        "Successfully logged out",
        icon='success',
        timer='2000',
        toast='true',
        position='top-end',
    )
    return redirect(reverse('home'))


# below code initially taken from a Code Institute
# tutorial and modified heavily for my project
def login(request):
    """
    If user is already logged in a message is displayed telling
    them this. If they fill in their details correctly they will
    be logged in, else the errors returned. If the user tried to
    access a page that requires loggin in then they will be directed
    to that 'next' page, else returned to home.
    """
    if request.user.is_authenticated:
        sweetify.success(
            request,
            "Already logged in!",
            icon='info',
            timer='1500',
            toast='true',
            position='center',
            background='#181818',
        )
        return redirect(reverse('home'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(
                username=request.POST['username'],
                password=request.POST['password']
            )
            if user:
                auth.login(user=user, request=request)
                sweetify.success(
                    request,
                    title="Welcome back " + user.username,
                    icon='success',
                    timer='2000',
                    toast='true',
                    position='top-end',
                )
                return redirect(request.GET.get('next', 'home'))
            else:
                login_form.add_error(None, "Username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


# below code initially taken from a Code Institute
# tutorial and modified heavily for my project
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
        sweetify.error(
            request,
            "Sure you're already registered!",
            icon='info',
            timer='1500',
            toast='true',
            position='center',
        )
        return redirect(reverse('home'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST, request.FILES)

        if registration_form.is_valid():
            registration_form.save()
            user = auth.authenticate(
                username=request.POST['username'],
                password=request.POST['password1']
            )
            pic = registration_form.cleaned_data['profile_pic']
            if not pic:
                pic = 'images/user.png'
            user.profile_pic = pic
            Profile.objects.create(
                user=user,
                username=request.POST['username'],
                profile_pic=pic
            )
            if user:
                auth.login(user=user, request=request)
                prev_url = request.POST.get('prevUrl')
                if prev_url == 'shop':
                    return redirect('view_cart')
                else:
                    sweetify.success(
                        request,
                        title='Thank you for registering, why not edit your:' +
                        '<a href="/accounts/profile/"><u>Profile Page</u></a>',
                        icon='success',
                        toast='true',
                        timer='11000',
                        position='center',
                    )
                    return redirect(reverse('home'))
            else:
                sweetify.error(
                    request,
                    "Unable to register your account at this time",
                    icon='warning',
                    timer='2000',
                    toast='true',
                    position='center',
                )
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
            sweetify.success(
                request,
                "Account details updated",
                icon='success',
                timer='3000',
                toast='true',
                position='bottom',
                background='#181818',
            )
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
            sweetify.success(
                request,
                "Profile picture updated",
                icon='success',
                timer='3000',
                toast='true',
                position='bottom',
                background='#181818',
            )
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
            sweetify.success(
                request,
                "Password updated",
                icon='success',
                timer='3000',
                toast='true',
                position='bottom',
                background='#181818',
            )
            return redirect('profile')
        else:
            sweetify.error(
                request,
                "Error, please correct",
                icon='success',
                timer='3000',
                toast='true',
                position='center',
            )
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password.html', {'form': form})
