from django.shortcuts import render
from base.models import *
import operator
from datetime import datetime

def home(request):
    club = Clubs.objects.all().order_by('?')
    for i in club:
        i.deadline = i.D_day(datetime.now())
    context = {'clubs':club} 
    if request.GET.get('rank'):
        rank = sorted(club,key=operator.attrgetter('club_rank')) # 우선순위 정렬
        context = {'clubs':rank}
    if request.GET.get('dday'):
        dday = sorted(club, key=operator.attrgetter('deadline')) #디데이 정렬
        context = {'clubs':dday}
    return render(request,'home.html',context)

# Create your views here.
