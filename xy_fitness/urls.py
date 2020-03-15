from django.conf.urls import url, include
from django.contrib import admin
from django.views import static
from pages.views import home_page
from pages import urls as urls_pages

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page, name='home'),
    url(r'^page/', include(urls_pages)),
]