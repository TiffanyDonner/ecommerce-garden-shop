from django.shortcuts import render
from products.models import Product


# Create your views here.
def do_search(request):
    products_name = Product.objects.filter(name__icontains=request.GET['q'])
    products_description = Product.objects.filter(description__icontains=request.GET['q'])
    products = products_name | products_description
    return render(request, "products.html", {"products": products})
