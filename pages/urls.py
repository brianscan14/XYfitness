from django.conf.urls import url
from .views import about, contact

urlpatterns = [
    url('about/', about, name="about"),
    url('contact/', contact, name="contact"),
]
