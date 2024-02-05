from unittest import TestCase
from django.test import Client, SimpleTestCase
from users.models import CustomUser
from django.urls import reverse,resolve
from django.utils import timezone
from users.views import CustomUserSignup,CustomUserLogin,CustomLogoutView,edit_profile,profile_view
# Create your tests here.


# Urlni test qilamiz
class TestUrls(SimpleTestCase):

    def test_login_url_is_resolved(self):
        url = reverse('login')
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class,CustomUserLogin)
        
    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class,CustomLogoutView)

    def test_sign_up_url_is_resolved(self):
        url = reverse('sign-up')
        self.assertEquals(resolve(url).func.view_class,CustomUserSignup)

    def test_edit_profile_url_is_resolved(self):
        url = reverse('edit-profile') # agar urlga pk yoki slug 
                                        # bo'yicha path yozilgan bo'sa (url = reverse('edit-profile',args=['some-slug']))
        self.assertEquals(resolve(url).func,edit_profile)
