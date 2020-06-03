from django.conf.urls import url
from .views import all_products, product_category, product_detail


urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^product/(?P<product_id>[0-9]+)', product_detail, name='product_detail'),
    url(r'^category/(?P<category>[A-Za-z]+)', product_category, name="product_category"),
]
