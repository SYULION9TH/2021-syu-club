from django.contrib import admin
from django.urls import path, include
from base.views import *

urlpatterns = [
    path('', index, name="index" ),
    path('home/', home, name="home"),
]