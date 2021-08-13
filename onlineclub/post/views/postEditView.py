from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from base.models import *


def edit(request, id):
    edit_post = Posts.objects.get(post_id=id)
    return render(request, 'post/edit.html', {'post':edit_post})

def update(request, id):
    update_post = Posts.objects.get(post_id=id)
    update_post.post_title = request.POST['post_title']
    update_post.post_content = request.POST['post_content']
    update_post.post_img_url = request.POST['post_img_url']
    update_post.post_img = request.POST['post_img']
    update_post.updated_at = timezone.now()
    update_post.save()
    return redirect('detail', str(update_post.post_id))