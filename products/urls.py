from django.conf.urls import url
from .views import all_prods, plans, apparel

urlpatterns = [
    url(r'^$', all_prods, name='products'),
    url(r'^plans/$', plans, name='plans'),
    url(r'^apparel/$', apparel, name='apparel'),
]