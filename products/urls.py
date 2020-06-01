from django.conf.urls import url
from .views import all_products, view_categories, product_detail


urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^product/', product_detail, name='product'),
    url(r'^category/<str:category>', view_categories, name="view_categories"),
]
