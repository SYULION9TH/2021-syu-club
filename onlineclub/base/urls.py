from django.contrib import admin
from django.urls import path, include
from base import views

urlpatterns = [
    path('', views.intro, name="intro"),
]

