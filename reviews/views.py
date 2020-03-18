from .models import Review
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.mixins import LoginRequiredMixin


def all_reviews(request):
    stuff = {
        'reviews': Review.objects.all()
    }
    return render(request, 'reviews.html', stuff)


def single_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    return render(request, 'single-review.html', {'review': review})


def new_review(request):
     return render(request, 'reviews.html')