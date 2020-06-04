from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'cafe', views.cafe, name="cafe"),
    url(r'pineapple', views.pineapple, name="pineapple"),
]
