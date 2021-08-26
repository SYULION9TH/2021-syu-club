from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from base.models import *
import os

def post_edit(request, club_id, id):
    edit_post = Posts.objects.get(club_id=club_id, post_id=id)
    return render(request, 'post/post_edit.html', {'post':edit_post, 'club_id':club_id})

def post_update(request, club_id, post_id):
    update_post = Posts.objects.get(post_id=post_id)
    update_post.post_title = request.POST['post_title']
    # update_post.post_content = request.POST['post_content']
    update_post.post_content = request.POST.get('post_content', 'post_content')
    update_post.post_img = request.FILES.get('post_img','post_img')
    update_post.updated_at = timezone.now()
    update_post.save()
    return redirect('detail', str(club_id), str(update_post.post_id))


def club(request):
    #동아리 이름과 동아리 한줄 설명 가져오기 위해서
    club = Clubs.objects.all()
    return render(request, 'home.html', {'club':club})



def detailpage_update(request, club_id):
    update_detailpage = Clubs.objects.get(club_id=club_id)

    if request.method =="POST":
        update_detailpage.club_img = request.FILES.get('club_img', 'club_img')
        # update_detailpage.club_img = request.FILES['club_img']
        update_detailpage.club_desc = request.POST.get('club_desc','club_desc')
        # update_detailpage.recruitment_content = request.POST['recruitment_content']
        update_detailpage.recruitment_content = request.POST.get('recruitment_content', 'recruitment_content')
        # update_detailpage.save(commit=False)
        update_detailpage.save()
        return redirect('home' , str(update_detailpage.club_id))

    else:
        return render(request,'post/update.html',{'club':update_detailpage, 'club_id':club_id})
