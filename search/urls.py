from django.conf.urls import url
from .views import search, cat_search, plans, apparel, sort


urlpatterns = [
    url(r'^$', search, name='search'),
    url(r'^categories/$', cat_search, name='cat_search'),
    url(r'^plans/$', plans, name='plans'),
    url(r'^apparel/$', apparel, name='apparel'),
    url(r'^sort/$', sort, name='sort')
]
