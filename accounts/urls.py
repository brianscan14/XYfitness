from django.conf.urls import url, include
from accounts import url_reset
from .views import (
    logout, login, register, profile, update_profile,
    update_password, update_profile_pic
)

urlpatterns = [
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^register/$', register, name='register'),
    url(r'^profile/update/$', update_profile, name='update_profile'),
    url(r'^profile/update/picture/$',
        update_profile_pic, name='update_profile_pic'
        ),
    url(r'^profile/update/password/$', update_password, name='update_password'),
    url(r'^password-reset/', include(url_reset)),
]