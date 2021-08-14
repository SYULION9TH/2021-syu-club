from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from base.models import *

# def detail(request, id):
#     club = get_object_or_404(Clubs, club_id=id)
#     return render(request, 'detail.html', {'club':club})

def post_edit(request, id):
    edit_post = Posts.objects.get(post_id=id)
    return render(request, 'post/edit.html', {'post':edit_post})

def post_update(request, id):
    update_post = Posts.objects.get(post_id=id)
    update_post.post_title = request.POST['post_title']
    update_post.post_content = request.POST['post_content']
    update_post.post_img = request.FILES.get('img','post_img')
    update_post.updated_at = timezone.now()
    update_post.save()
    return redirect('detail', str(update_post.post_id))


def club(request):
    #동아리 이름과 동아리 한줄 설명 가져오기 위해서
    club = Clubs.objects.all()
    return render(request, 'home.html', {'club':club})



def detailpage_update(request, id):
    update_detailpage = Clubs.objects.get(club_id=id)

    if request.method =="POST":
        
        update_detailpage.club_img = request.FILES.get('img','club_img')
        update_detailpage.club_desc = request.POST.get('desc','club_desc')
        update_detailpage.recruitment_content = request.POST.get('recruitment','recruitment_content')
        update_detailpage.save()
        return redirect('detail' , str(update_detailpage.club_id))

    else:
        return render(request,'edit.html',{'club':update_detailpage})

