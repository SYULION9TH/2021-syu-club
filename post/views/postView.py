from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from base.models import *


def home(request, club_id):
    # posts = Posts.objects.get()
    posts = Posts.objects.filter(club_id=club_id)
    club = Clubs.objects.get(club_id=club_id)
    return render(request, 'post/home.html', {'posts':posts, 'club_id':club_id, 'club':club})

def detail(request, club_id, id):
    post = get_object_or_404(Posts, club_id=club_id, post_id=id)
    return render(request, 'post/post_detail.html', {'post':post, 'club_id':club_id})

def new(request, club_id):
    return render(request, 'post/post_new.html', {'club_id':club_id})

def create(request, club_id):
    new_post = Posts()
    new_post.post_title = request.POST['post_title']
    new_post.post_content = request.POST['post_content']
    # new_post.post_img_url = request.POST['post_img_url'] # CharField 일 경우
    new_post.post_img = request.FILES['post_img'] # ImageField 일 경우
    new_post.created_at = timezone.now()
    new_post.updated_at = timezone.now()
    new_post.is_deleted = 0
    new_post.club = Clubs.objects.get(club_id=club_id)
    new_post.save()
    return redirect('detail', str(club_id), str(new_post.post_id))

def delete(request, club_id, id):
    delete_post = Posts.objects.get(club_id=club_id, post_id=id)
    delete_post.is_deleted = 1
    delete_post.delete()
    return redirect('home', str(club_id))
