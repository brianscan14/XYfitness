from django.conf.urls import url
from django.contrib import admin
from django.views import static
from pages.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
]
