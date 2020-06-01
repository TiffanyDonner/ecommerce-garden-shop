from django.shortcuts import render
from .models import Product


# Create your views here.
def all_products(request):
    """ Return and render all products """
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def product_detail(request):
    """ Return and render all products """
    products = Product.objects.all()
    return render(request, "product_detail.html", {"products": products})


def view_categories(request, category):
    """ Fetches all items belonging to a certain category. """

    categories = dict(Product.CATEGORY)
    categories = categories.values()

    products = Product.objects.filter(category=category)
    return render(request, 'products.html', {
        'products': products,
        'categories': categories})
