from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from base.models import *


def home(request):
    posts = Posts.objects.all()
    return render(request, 'post/home.html', {'posts':posts})

def detail(request, id):
    post = get_object_or_404(Posts, post_id=id)
    return render(request, 'post/detail.html', {'post':post})

def new(request):
    return render(request, 'post/new.html')

def create(request):
    new_post = Posts()
    new_post.post_title = request.POST['post_title']
    new_post.post_content = request.POST['post_content']
    new_post.post_img_url = request.POST['post_img_url'] # CharField 일 경우
    # new_post.post_img_url = request.FILES['post_img_url'] # ImageField 일 경우
    new_post.created_at = timezone.now()
    new_post.updated_at = timezone.now()
    new_post.is_deleted = 0
    new_post.save()
    return redirect('detail', str(new_post.post_id))

def delete(request, id):
    delete_post = Posts.objects.get(post_id=id)
    delete_post.is_deleted = 1
    delete_post.delete()
    return redirect('home')