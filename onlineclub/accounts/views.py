from django.shortcuts import render, redirect
from .models import *
# from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def login(request):
    # 관리자 로그인
    ## form.cleaned_date.get
    if (request.method == 'POST'):
        form = AuthenticationForm(request=request, data = request.POST)

        if (form.is_valid()):
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request=request, username = username, password = password)
            if (user is not None):
                login(request, user)
                return redirect('#') # TODO - to redirect HOME.html
            else : 
                # TODO - if user is None
                print("Login Fail!")

def logout(request):
    # 관리자 로그아웃
    logout(request)
    return redirect('#') # TODO - to redirect HOME.html