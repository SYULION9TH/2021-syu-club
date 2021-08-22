from django.db import models
from datetime import date


# user 테이블
class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()

    # class Meta:
    #     managed = False
    #     db_table = 'auth_user'


class ClubTypes(models.Model):
    club_type_id = models.AutoField(primary_key=True)
    club_type_name = models.CharField(max_length=200, blank=True, null=True)
    club_type_desc = models.CharField(max_length=200, blank=True, null=True)
    club_type = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.club_type_name

    # class Meta:
    #     managed = False
    #     db_table = 'club_types'


# 동아리 모델 
class Clubs(models.Model):
    club_id = models.AutoField(primary_key=True)
    club_name = models.CharField(max_length=200, blank=True, null=True)
    main_club = models.IntegerField(blank=True, null=True)
    club_desc = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    club_type = models.ForeignKey(ClubTypes, models.DO_NOTHING)
    club_img = models.ImageField(upload_to='images/', blank=True, null=True) # 활동사진
    # club_logo_url = models.CharField(max_length=500, blank=True, null=True)
    club_logo = models.ImageField(upload_to='images/', blank=True, null=True) #로고
    # established = models.DateTimeField()
    # created_at = models.DateTimeField()
    # updated_at = models.DateTimeField()
    # end_day = models.DateTimeField(blank=True, null=True)
    # deadline = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    sns_link = models.CharField(max_length=500, blank=True, null=True) # 여분
    instagram_link = models.CharField(max_length=500, blank=True, null=True)
    facebook_link = models.CharField(max_length=500, blank=True, null=True)
    youtube_link = models.CharField(max_length=500, blank=True, null=True)
    form_link = models.CharField(max_length=500, blank=True, null=True)
    recruitment_content = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.club_name

    # def D_day(self,now):
    #     return int((self.end_day - now).days)

    # class Meta:
    #     managed = False
    #     db_table = 'clubs'


# 게시글 모델
class Posts(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=150)
    post_content = models.CharField(max_length=3000, blank=True, null=True)
    # post_introduce = models.CharField(max_length=200, blank=True, null=True)
    # post_img_url = models.CharField(max_length=1500, blank=True, null=True)
    post_img = models.ImageField(upload_to="post/", blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    # is_deleted = models.IntegerField(blank=True, null=True)
    club = models.ForeignKey(Clubs, models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return str(self.club)
    
    # class Meta:
    #     managed = False
    #     db_table = 'posts'


# 모집요강 테이블
# class Recruitment(models.Model):
#     recruitment_id = models.AutoField(primary_key=True)
#     recruitment_content = models.TextField(blank=True, null=True)
#     start_date = models.DateTimeField()
#     end_date = models.DateTimeField()
#     is_staff = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'recruitment'

