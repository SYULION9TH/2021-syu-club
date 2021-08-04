from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class AuthUser(models.Model):
    password = models.CharField(max_length=128) # 비밀번호
    last_login = models.DateTimeField(blank=True, null=True) # 마지막 로그인 일자
    is_superuser = models.IntegerField() # 슈퍼 유저
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField() # 스태프
    is_active = models.IntegerField() # ??
    date_joined = models.DateTimeField() # 가입 일자

    class Meta:
        managed = False # django migration 미허용
        db_table = 'auth_user'
