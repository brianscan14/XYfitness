from django.conf.urls import url
from .views import reviews

urlpatterns = [
    url(r'^reviews/$', reviews, name='reviews'),
]