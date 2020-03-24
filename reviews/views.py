from .models import Review
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostReviewForm
from django.contrib import messages
from django.db import IntegrityError


def all_reviews(request):
    reviews = {
        'reviews': Review.objects.all().order_by('-date')
    }
    return render(request, 'reviews.html', reviews)


def single_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    return render(request, 'single-review.html', {'review': review})


@login_required()
def new_review(request, pk=None):
    review = get_object_or_404(Review, pk=pk) if pk else None
    if request.method == "POST":
        form = PostReviewForm(request.POST, request.FILES, instance=review)
        form.instance.author = request.user
        form.instance.image = request.user.profile.profile_pic
        if form.is_valid():
            try:
                review = form.save()
                return redirect(single_review, review.pk)
            except IntegrityError:
                messages.success(request, "You already have a review!")
                return redirect(all_reviews)
    else:
        form = PostReviewForm(instance=review)
        form.instance.author = request.user
        form.instance.image = request.user.profile.profile_pic
    return render(request, 'addreview.html', {'form': form})


@login_required()
def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if review.author == request.user:
        review.delete()
        messages.success(request, "Your review was deleted")
        return redirect(all_reviews)
