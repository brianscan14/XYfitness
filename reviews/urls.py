from django.conf.urls import url
from .views import single_review, all_reviews, new_review

urlpatterns = [
    url(r'^$', all_reviews, name='all_reviews'),
    url(r'review/(?P<pk>\d+)', single_review, name='single_review'),
    url(r'^new/', new_review, name='new_review')
]
