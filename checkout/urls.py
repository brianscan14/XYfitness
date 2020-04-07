from django.conf.urls import url
from .views import checkout, delivery, order_confirm

urlpatterns = [
    url(r'^order/$', checkout, name='checkout'),
    url(r'^deliver/$', delivery, name='delivery'),
    url(r'^order.confirmation/$', order_confirm, name='order_confirm')
]