from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # path('', html, name='html'),
    path('loginhtml', loginhtml, name="loginhtml"),
    path('login', logining, name="login"),
    path('logout', logoutting, name="logout"),
    # path('register', register, name="register"),
]