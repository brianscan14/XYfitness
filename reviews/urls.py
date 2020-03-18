from django.conf.urls import url
from .views import single_review, all_reviews, new_review, delete_review

urlpatterns = [
    url(r'^$', all_reviews, name='all_reviews'),
    url(r'review/(?P<pk>\d+)', single_review, name='single_review'),
    url(r'^new/', new_review, name='new_review'),
    url(r'^(?P<pk>\d+)/edit/$', new_review, name='edit_review'),
    url(r'^(?P<pk>\d+)/delete/$', delete_review, name='delete_review')
]
