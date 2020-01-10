from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', doctor_login, name='login'),
    path('logout/', doctor_logout, name='logout'),
    path('register/', register, name='register'),
]