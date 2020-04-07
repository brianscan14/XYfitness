from django.conf.urls import url
from .views import checkout, delivery

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
    url(r'^deliver/$', delivery, name='delivery'),
]