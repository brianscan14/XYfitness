from django.conf.urls import url
from .views import search, cat_search, LtoH


urlpatterns = [
    url(r'^$', search, name='search'),
    url(r'^categories/$', cat_search, name='cat_search'),
    url(r'^LtoH/$', LtoH, name='LtoH')
]
