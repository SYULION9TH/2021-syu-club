from django.urls import path
from post.views import postView, postEditView

urlpatterns = [
    path('', postView.home, name="home"),
    path('<int:id>', postView.detail, name="detail"),
    path('new/', postView.new, name="new"),
    path('create/', postView.create, name="create"),
    path('<int:id>/delete', postView.delete, name="delete"),
    path('edit/<int:id>', postEditView.post_edit, name="edit"),
    path('<int:post_id>/update', postEditView.post_update, name="update"),
    #모집요강
    path('edit/', postEditView.detailpage_update, name="detailupdate"),    
]