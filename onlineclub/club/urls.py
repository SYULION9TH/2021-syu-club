from django.contrib import admin
from django.urls import path, include
from club import views

urlpatterns = [
    path('', views.home1, name="home1"),
    path('<int:club_type>', views.haksool, name="haksool"),
    path('post/<int:club_id>/', include('post.urls')),
]
