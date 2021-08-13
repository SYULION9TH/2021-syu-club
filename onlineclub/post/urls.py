from django.contrib import admin
from django.urls import path, include
from post.views import postView, postEditView

urlpatterns = [
    path('<int:id>/edit', postEditView.detailpage_update, name="detailupdate"),
    path('<int:id>/<int:post_id>/post_edit', postEditView.post_update ,name="postupdate"),
]