<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
from django.shortcuts import render, get_object_or_404
from base.models import *
from django.db.models import Q
import operator
from datetime import datetime

def home1(request):
    template_name='club/home.html'
    club_list = Clubs.objects.all().order_by('?')
    #  사이드메뉴 (문화 학술 봉사)
    side_menu1 = Clubs.objects.all().filter(club_type = 1)
    side_menu2 = Clubs.objects.all().filter(club_type = 2)
    side_menu3 = Clubs.objects.all().filter(club_type = 3)
            
    # 검색어 유
    if request.GET.get("keyword"):
        keyword = request.GET.get("keyword")
        club_list = Clubs.objects.filter(Q(club_name__icontains = keyword)).distinct()
        # return render(request, 'club/home.html', {'club_list': club_list})
    # 검색어 무
    # else:
    #     club_list = Clubs.objects.all().order_by('?')
    #     return render(request, 'club/home.html', {'club_list': club_list, 'side_menu1':side_menu1, 'side_menu2':side_menu2, 'side_menu3':side_menu3})

    for club in club_list:
        club.deadline = club.D_day(datetime.now())
    if request.GET.get('rank'):
        # rank = sorted(club_list, key=operator.attrgetter('rank')) # 우선순위 정렬
        # context = {'clubs':rank}
        club_list = sorted(club_list, key=operator.attrgetter('rank'))
        # return render(request, 'club/home.html', context)
    if request.GET.get('dday'):
        # dday = sorted(club_list, key=operator.attrgetter('deadline'), reverse=True) #디데이 정렬
        # context = {'clubs':dday}
        club_list = sorted(club_list, key=operator.attrgetter('deadline'), reverse=True)
        # return render(request, 'club/home.html', context)
    return render(request, template_name, {'club_list':club_list}) 

# 동아리 분과별
def haksool(request, club_type):
    template_name = 'club/haksool.html'
    # 사이드메뉴 (문화 학술 봉사)
    side_menu1 = Clubs.objects.all().filter(club_type = 1)
    side_menu2 = Clubs.objects.all().filter(club_type = 2)
    side_menu3 = Clubs.objects.all().filter(club_type = 3)

    # 검색어 유
    if request.GET.get("keyword"):
        keyword = request.GET.get("keyword")
        club_list = Clubs.objects.all().filter(Q(club_type = club_type) & (Q(club_name__icontains = keyword)))
        return render(request, template_name, {'club_list': club_list, 'club_type': club_type, 'side_menu1':side_menu1, 'side_menu2':side_menu2, 'side_menu3':side_menu3})
    # 검색어 무
    else:
        club_list = Clubs.objects.all().filter(club_type = club_type).order_by('club_name')
        return render(request, template_name, {'club_list': club_list, 'club_type': club_type, 'side_menu1':side_menu1, 'side_menu2':side_menu2, 'side_menu3':side_menu3})
>>>>>>> 3521c9d2bc4740bda1e2a48cdbc626a27f10bcf5
