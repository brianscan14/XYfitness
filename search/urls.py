from django.conf.urls import url
from .views import search, cat_search, sort


urlpatterns = [
    url(r'^$', search, name='search'),
    url(r'^categories/$', cat_search, name='cat_search'),

    url(r'^sort/$', sort, name='sort')
]
