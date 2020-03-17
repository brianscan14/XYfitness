from .models import Review
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def all_reviews(request):
    stuff = {
        'reviews': Review.objects.all()
    }
    return render(request, 'reviews.html', stuff)


class ReviewListView(ListView):
    model = Review
    template_name = 'reviews.html'
    context_object_name = 'reviews'
    ordering = ['-date']


class ViewReview(DetailView):
    model = Review
    template_name = 'review_detail.html'
    context_object_name = 'review'


class CreateReview(LoginRequiredMixin, CreateView):
    model = Review
    template_name = 'review_form.html'
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
