from django.conf.urls import url, include
from .views import index, about, contact, products, testimonials

urlpatterns = [
    url('about/', about, name="about"),
    url('contact/', contact, name="contact"),
    url('products/', products, name="products"),
    url('testimonials/', testimonials, name="testimonials")
]