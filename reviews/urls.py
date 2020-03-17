from django.conf.urls import url
from .views import all_reviews

urlpatterns = [
    url(r'^$', all_reviews, name='all_reviews'),
]
