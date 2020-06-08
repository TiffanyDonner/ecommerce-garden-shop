from django.shortcuts import render, redirect, reverse


# Create your views here.
def view_cart(request):
    """ Simple view to render cart items """
    return render(request, 'cart.html')


def add_to_cart(request, id):
    """ Request quanity of items to cart """
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return render(request, "cart.html")


def adjust_cart(request, id):
    """ Call quanity to cart and request the adjustment to cart  """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
