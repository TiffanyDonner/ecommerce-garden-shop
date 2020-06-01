from django.conf.urls import url
from .views import all_products, view_categories


urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^category/<str:category>', view_categories, name="view_categories"),
]
