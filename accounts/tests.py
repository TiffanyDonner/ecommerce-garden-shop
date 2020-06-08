from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth import views as auth_views


# Create your tests here.
class TestUrls(SimpleTestCase):

    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, auth_views.LoginView)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func.view_class, auth_views.LogoutView)
