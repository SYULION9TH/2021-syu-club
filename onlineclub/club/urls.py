from django.contrib import admin
from django.urls import path, include
from club import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:club_type>', views.haksool, name="haksool"),
]