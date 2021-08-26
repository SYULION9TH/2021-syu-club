from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
# from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

from .forms import SigninForm

# Testing
def loginhtml(request):
    form = SigninForm()
    return render(request, 'accounts/login.html', {'form': form})

# 관리자 로그인
def logining(request):
    if (request.method == 'POST'):
        form = AuthenticationForm(request=request, data = request.POST)

        if (form.is_valid()):
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request=request, username = username, password = password)
            if (user is not None):
                login(request, user)
                print("Login Succeed!")
                return redirect('/club') # TODO - to redirect HOME.html
        else:
            # TODO - if user is None
            print("Login Fail!")
            return redirect('accounts/loginhtml') # 틀리면 다시 loginhtml 실행!
## 관리자 로그인 - 로그아웃 
def logoutting(request):
    logout(request)
    return redirect('/club') # TODO - to redirect HOME.html

# # 회원가입
# def register(request):
#     if (request.method == 'POST'):
#         if (request.POST['password'] == request.POST['repassword']):
#             clean_username(request, request.POST['username'])
#             user = User.objects.create_user(email = request.POST['email'], password = request.POST['password'], username = request.POST['username'])
#             user.save()
#             return request('login')
#         return render(request, 'register.html', {'error': "Password did not matched\n비밀번호가 맞지 않습니다."})
#     return render(request, 'register.html')
# ## 회원가입 - 중복 검사
# def clean_username(request, username):
#     user_model = get_user_model() # your way of getting the User
#     try:
#         user_model.objects.get(username__iexact=username)
#     except user_model.DoesNotExist:
#         return username
#     raise render(request,"This username has already existed.\n해당 아이디는 이미 사용 중입니다.")