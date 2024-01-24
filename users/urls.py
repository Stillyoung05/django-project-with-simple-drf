from django.urls import path
from .views import sign_up_view,login_view,homepage_view,profile_view,edit_profile,logout_view

urlpatterns = [
    path('sign-up',sign_up_view,name='sign-up'),
    path('',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('home/',homepage_view,name='home'),
    path('profile/',profile_view,name='profile'),
    path('edit-profile/',edit_profile,name='edit-profile')


]