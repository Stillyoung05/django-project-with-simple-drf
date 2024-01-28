from django.urls import path
from .views import CustomUserSignup,CustomUserLogin,homepage_view,profile_view,edit_profile,CustomLogoutView
# app_name = 'users'

urlpatterns = [
    path('sign-up',CustomUserSignup.as_view(),name='sign-up'),
    path('',CustomUserLogin.as_view(),name='login'),
    path('logout/',CustomLogoutView.as_view(),name='logout'),
    path('home/',homepage_view,name='home'),
    path('profile/',profile_view,name='profile'),
    path('edit-profile/',edit_profile,name='edit-profile')


]