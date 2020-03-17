from django.conf.urls import url
from .views import ViewReview, CreateReview, ReviewListView

urlpatterns = [
    url(r'^$', ReviewListView.as_view(), name='all_reviews'),
    url(r'review/(?P<id>\d+)', ViewReview.as_view(), name='review'),
    url(r'^new/', CreateReview.as_view(), name='new_review')
]
