from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # path('', html, name='html')
    path('login', login, name="login"),
    path('logout', logout, name="logout"),
    path('register', register, name="register"),
]