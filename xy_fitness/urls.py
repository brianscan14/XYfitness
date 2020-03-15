from django.conf.urls import url, include
from django.contrib import admin
from django.views import static
from pages.views import index
from pages import urls as urls_pages

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^page/', include(urls_pages)),
]
