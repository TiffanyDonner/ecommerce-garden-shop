from django.conf.urls import url
from .views import checkout, order_complete

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
    url(r'^order-complete/', order_complete, name='order_complete'),
]
