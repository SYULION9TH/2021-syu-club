from django.shortcuts import render
from base.models import Clubs
from django.db.models import Q

# Create your views here.

# 동아리 전체
def home(request):
    template_name = 'home.html'
    # 사이드메뉴 (학술 봉사 문화)
    side_menu1 = Clubs.objects.all().filter(club_type = 1)
    side_menu2 = Clubs.objects.all().filter(club_type = 2)
    side_menu3 = Clubs.objects.all().filter(club_type = 3)
            
    # 검색어 유
    if request.GET.get("keyword"):
        keyword = request.GET.get("keyword")
        club_list = Clubs.objects.filter(Q(club_name__icontains = keyword) | Q(club_desc__icontains = keyword)).distinct()
        return render(request, template_name, {'club_list': club_list})
    # 검색어 무
    else:
        club_list = Clubs.objects.all()
        return render(request, template_name, {'club_list': club_list, 'side_menu1':side_menu1, 'side_menu2':side_menu2, 'side_menu3':side_menu3})

# 동아리 분과별
def haksool(request, club_type):
    template_name = 'haksool.html'
    # 사이드메뉴 (학술 봉사 문화)
    side_menu1 = Clubs.objects.all().filter(club_type = 1)
    side_menu2 = Clubs.objects.all().filter(club_type = 2)
    side_menu3 = Clubs.objects.all().filter(club_type = 3)

    # 검색어 유
    if request.GET.get("keyword"):
        keyword = request.GET.get("keyword")
        club_list = Clubs.objects.all().filter(Q(club_type = club_type) & (Q(club_name__icontains = keyword) | Q(club_desc__icontains = keyword)))
        return render(request, template_name, {'club_list': club_list, 'club_type': club_type, 'side_menu1':side_menu1, 'side_menu2':side_menu2, 'side_menu3':side_menu3})
    # 검색어 무
    else:
        club_list = Clubs.objects.all().filter(club_type = club_type).order_by('club_name')
        return render(request, template_name, {'club_list': club_list, 'club_type': club_type, 'side_menu1':side_menu1, 'side_menu2':side_menu2, 'side_menu3':side_menu3})