from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages


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


# Code modeled from Codemy.com [Contact Pages](https://www.youtube.com/watch?v=w4ilq6Zk-08)
def contact(request):
    """Returns the contact file"""
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send an email
        send_mail(
            'message from ' + message_name,  # subject
            message,  # message
            message_email,  # from eamil
            ['leilynn78@gmail.com'],  # to email
        )
        messages.success(request,
                         "Thank you! We have received your email and will respond shortly..."
                         )

        return render(request, 'contact.html', {'message_name': message_name})

    else:
        return render(request, 'contact.html', {})
