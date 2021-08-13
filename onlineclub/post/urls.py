from django.contrib import admin
from django.urls import path, include
from post.views import postView, postEditView

urlpatterns = [
    #게시물
    path('<int:id>', postView.home, name="home"),
    path('<int:id>/<int:post_id>', postView.detail, name="detail"),
        # 단순히 new.html연결
    path('<int:id>/new/', postView.new, name="new"),
    path('<int:id>/create/', postView.create, name="create"),
    path('<int:id>/<int:post_id>/post_edit', postEditView.post_update ,name="postupdate"),
    path('<int:id>/<int:post_id>/update', postEditView.update, name="update"),
    path('<int:id>/<int:post_id>/delete', postView.delete, name="delete"),
    #모집요강
    path('<int:id>/edit', postEditView.detailpage_update, name="detailupdate"),

]