from django.conf.urls import url, include
from .views import home_page, about, contact, testimonials

urlpatterns = [
    url('about/', about, name="about"),
    url('contact/', contact, name="contact"),
    url('testimonials/', testimonials, name="testimonials")
]