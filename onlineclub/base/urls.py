from django.contrib import admin
from django.urls import path, include
from base.views import *

urlpatterns = [
    path('', home , name="home" )
]