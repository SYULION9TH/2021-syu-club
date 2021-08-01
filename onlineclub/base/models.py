from django.db import models
from datetime import date
#user 테이블

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class ClubTypes(models.Model):
    club_type_id = models.AutoField(primary_key=True)
    club_type_name = models.IntegerField(blank=True, null=True)
    club_type_desc = models.CharField(max_length=200, blank=True, null=True)
    club_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'club_types'



# 동아리 모델 
class Clubs(models.Model):
    club_id = models.AutoField(primary_key=True)
    club_name = models.CharField(max_length=200, blank=True, null=True)
    club_desc = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    club_type = models.ForeignKey(ClubTypes, models.DO_NOTHING)
    club_img_url = models.CharField(max_length=500, blank=True, null=True) #활동사진
    club_logo_url = models.CharField(max_length=500, blank=True, null=True)
    established = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    end_day = models.DateTimeField()
    deadline = models.IntegerField()
    sns_link = models.CharField(max_length=500, blank=True, null=True)
    form_link = models.CharField(max_length=500, blank=True, null=True)
    
    def D_day(self,now):
        return int((self.end_day - now).days)

    class Meta:
        managed = False
        db_table = 'clubs'

#계시글 모델
class Posts(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=150)
    post_content = models.CharField(max_length=3000)
    post_introduce = models.CharField(max_length=200, blank=True, null=True)
    post_img_url = models.CharField(max_length=1500, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_deleted = models.IntegerField()
    club = models.ForeignKey(Clubs, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'posts'


# 모집요강 테이블

class Recruitment(models.Model):
    recruitment_id = models.AutoField(primary_key=True)
    recruitment_content = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_staff = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recruitment'

