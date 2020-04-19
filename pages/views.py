from django.shortcuts import render, redirect
from .forms import EmailContactForm
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from reviews.models import Review
from .models import Query


def home_page(request):
    """
    Returns index page, testimonials added so
    that the user can see them on this page in a 
    slideshow
    """
    reviews = {
        'reviews': Review.objects.all().order_by('-date')
    }
    return render(request, "index.html", reviews)


def about(request):
    """Returns about page giving more info about the PT"""
    return render(request, "about.html")


def contact(request):
    """
    Uses Django mails to send mail to owner, also creates a
    mail in the admin site to view it there.
    """
    if request.method == 'GET':
        if request.user.is_authenticated:
            form_filled = {
                'email': request.user.email
            }
            form = EmailContactForm(initial=form_filled)
        else:
            form = EmailContactForm()
    else:
        form = EmailContactForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(title, message, email, ['admin@hotmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, "Successfully sent mail")
            query = Query(
                title=title,
                email=email,
                message=message
            )
            query.save()
            return redirect('home')
    return render(request, "contact.html", {'form': form})
