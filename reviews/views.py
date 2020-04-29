from .models import Review
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostReviewForm
from django.db import IntegrityError
import sweetify
import datetime


def all_reviews(request):
    """Return all testimonials added to the page, order newest first."""
    reviews = {
        'reviews': Review.objects.all().order_by('-date')
    }
    return render(request, 'reviews.html', reviews)


def single_review(request, pk):
    """Return view of a single testimonial."""
    review = get_object_or_404(Review, pk=pk)
    return render(request, 'single-review.html', {'review': review})


# below code taken from a Code Institute tutorial and modified for my project
@login_required()
def new_review(request, pk=None):
    """
    Either add a new testimonial or edit a previous review on the page
    if the user is the testimonial author.
    """
    review = get_object_or_404(Review, pk=pk) if pk else None
    if request.method == "POST":
        form = PostReviewForm(request.POST, request.FILES, instance=review)
        form.instance.author = request.user
        form.instance.date = datetime.datetime.now()
        form.instance.image = request.user.profile.profile_pic
        if form.is_valid():
            try:
                review = form.save()
                sweetify.success(
                    request,
                    "Thanks a million for your Testimonial!",
                    icon='success',
                    timer='2500',
                    toast='true',
                    position='top',
                )
                return redirect(single_review, review.pk)
            except IntegrityError:
                sweetify.error(
                    request,
                    "You already made a Testimonial!",
                    icon='info',
                    timer='3000',
                    toast='true',
                    position='center',
                    background='#181818',
                )
                return redirect(all_reviews)
    else:
        form = PostReviewForm(instance=review)
        form.instance.author = request.user
        form.instance.date = datetime.datetime.now()
        form.instance.image = request.user.profile.profile_pic
    return render(request, 'addreview.html', {'form': form})


@login_required()
def delete_review(request, pk):
    """Remove testimonial from the page if the user is the author."""
    review = get_object_or_404(Review, pk=pk)
    if review.author == request.user:
        review.delete()
        sweetify.error(
            request,
            "Testimonial deleted :(",
            icon='success',
            timer='2500',
            toast='true',
            position='center',
            background='#181818',
        )
        return redirect(all_reviews)
