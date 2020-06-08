from django.conf.urls import url, include
from accounts.views import (
    logout,
    login,
    registration,
    user_profile,
    edit_profile,
    change_password,
)

from django.contrib.auth.views import (
    password_reset, password_reset_done, password_reset_confirm,
    password_reset_confirm, password_reset_complete,
)    


urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="registration"),
    url(r'^profile/', user_profile, name="profile"),
    url(r'^edit/$', edit_profile, name="edit_profile"),
    url(r'^password/', change_password, name="change_password"),
    url(r'^reset-password/', password_reset, name='reset_password'),
    url(r'^reset-password/done/', password_reset_done, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/',
        password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset-password/complete/', password_reset_complete,
        name='password_reset_complete'),
]
