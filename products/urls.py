from django.conf.urls import url
from .views import all_prods

urlpatterns = [
    url(r'^$', all_prods, name='products'),
]