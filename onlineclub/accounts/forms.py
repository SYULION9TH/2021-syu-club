# forms?
from django.db import models
from django.db.models import fields
from base.models import AuthUser
from django import forms

# create forms.py
# class SignupForm(forms.ModelForm):
#     class Meta:
#         model = AuthUser # It is model's name
#         fields = ['email', 'password', 'username']

class SigninForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = ['username', 'password']
    
    username = forms.CharField( # 1
        error_messages={
            'required': "아이디를 입력해주세요."
        },
        max_length=150,
        label="ID"
    )
    password = forms.CharField( #2
        error_messages={
            'required': "비밀번호를 입력해주세요."
        },
        max_length=128,
        widget=forms.PasswordInput,
        label="Password"
    )