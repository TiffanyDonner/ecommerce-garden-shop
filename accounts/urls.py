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
from accounts import url_reset


urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="registration"),
    url(r'^profile/', user_profile, name="profile"),
    url(r'^edit/$', edit_profile, name="edit_profile"),
    url(r'^password/', change_password, name="change_password"),
    url(r'^password-reset/', include(url_reset))

]
