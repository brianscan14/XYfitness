from django.shortcuts import render
from .models import Review


# Create your views here.
def all_reviews(request):
    stuff = {
        'reviews': Review.objects.all()
    }
    return render(request, 'reviews.html', stuff)
