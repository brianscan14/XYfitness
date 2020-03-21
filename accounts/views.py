from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import UserLoginForm, UserRegistrationForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Profile


def all_links(request):
    return render(request,  'all-links.html')


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "Successfully logged out")
    return redirect(reverse('home'))


def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        messages.success(request, "Already logged in!")
        return redirect(reverse('home'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            messages.success(request, "You have successfully logged in!")

            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('home'))
            else:
                login_form.add_error(None, "Username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def register(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        messages.success(request, "Sure you're already registered! :)")
        return redirect(reverse('home'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            Profile.objects.create(
                user=user,
                username=request.POST['username']
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
        "registration_form": registration_form})


@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account updated.')
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'update.html', {
        "form": form})
