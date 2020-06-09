from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm, EditProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from checkout.models import OrderLineItem


def index(request):
    """Simple return index"""
    return render(request, 'index.html')


@login_required
def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('index'))


def login(request):
    """Verifys user and returns login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)

        """ If user criteria is valid login user and send then to cart """
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            messages.success(request, "You have successfully logged in!")

            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('view_cart'))
            else:
                login_form.add_error(None,
                                     "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def registration(request):
    """Render the registration page and validate criteria"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered.")
                return redirect(reverse('view_cart'))
            else:
                messages.error(request,
                               "Unable to register your account at this time.")
                return redirect(reverse('register'))
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
        'registration_form': registration_form})


def user_profile(request):
    """ Pull user database information to page """
    user = User.objects.get(
        email=request.user.email,
        first_name=request.user.first_name,
        last_name=request.user.last_name
        )

    orders = user.orders.all()

    order = OrderLineItem.objects.filter()

    return render(request, 'profile.html', {'profile': user, 'orders': orders, 'order': order,})


def edit_profile(request):
    """ Request User instance to edit profile """
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Profile has been updated.")
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)


# Code modeled from Max Goodridge [Django Tutorial](https://www.youtube.com/watch?v=JmaxoPBvp1M&list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj&index=18)
def change_password(request):
    """ Change password for logged in user """
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST,
                                  user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Your password was updated!")
            return redirect('profile')
        else:
            messages.success(request, "Please check your password and try again.")
            return redirect('change_password')

    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'change_password.html', args)
