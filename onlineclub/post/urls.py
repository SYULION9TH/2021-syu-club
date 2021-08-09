from django.urls import path
from post.views import postView, postEditView

urlpatterns = [
    path('', postView.home, name="home"),
    path('<int:id>', postView.detail, name="detail"),
    path('new/', postView.new, name="new"),
    path('create/', postView.create, name="create"),
    # path('edit/<int:id>', postEditView.edit, name="edit"),
    # path('<int:id>/update', postEditView.update, name="update"),
    path('<int:id>/delete', postView.delete, name="delete"),
]