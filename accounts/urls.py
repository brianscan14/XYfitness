from django.conf.urls import url, include
from .views import all_links, logout, login, register

urlpatterns = [
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^register/$', register, name='register'),
    url(r'^all/links/$', all_links, name='all-links'),
]