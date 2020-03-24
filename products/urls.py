from django.conf.urls import url
from .views import all_prods, plans, apparel, sort, sort_apparel, sort_plans, single_prod, review_prod, delete_prod_review, edit_review_prod

urlpatterns = [
    url(r'^$', all_prods, name='products'),
    url(r'product/(?P<pk>\d+)', single_prod, name='single_prod'),
    url(r'product/review/(?P<pk>\d+)/$', review_prod, name='review_prod'),
    url(r'product/review/edit/(?P<pk>\d+)/$', edit_review_prod, name='edit_review_prod'),
    url(r'^(?P<pk>\d+)/delete/$', delete_prod_review, name='delete_prod_review'),
    url(r'^plans/$', plans, name='plans'),
    url(r'^apparel/$', apparel, name='apparel'),
    url(r'^sort/$', sort, name='sort'),
    url(r'^apparel/sort/$', sort_apparel, name='sort_apparel'),
    url(r'^plans/sort/$', sort_plans, name='sort_plans')
]