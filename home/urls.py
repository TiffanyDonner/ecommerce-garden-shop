from django.conf.urls import url
from . import views
from home.views import index

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'cafe', views.cafe, name="cafe"),
    url(r'pineapple', views.pineapple, name="pineapple"),
    url(r'contact', views.contact, name="contact"),
]
