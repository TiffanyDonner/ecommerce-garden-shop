from django.shortcuts import render


# Create your views here.
def index(request):
    """A view that displays the index page"""
    return render(request, "index.html")


def cafe(request):
    """Returns the cafe file"""
    return render(request, 'cafe.html')


def pineapple(request):
    """Returns the grow_pineapple file"""
    return render(request, 'grow_pineapple.html')
