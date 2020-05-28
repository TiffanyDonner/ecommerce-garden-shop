from django.shortcuts import render
from .models import Product


# Create your views here.
def all_products(request):
    """ Return and render all products """
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})
