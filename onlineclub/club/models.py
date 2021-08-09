from django.db import models

# Create your models here.

class ClubTypes(models.Model):
    club_type_id = models.AutoField(primary_key=True)
    club_type_name = models.IntegerField(blank=True, null=True)
    club_type_desc = models.CharField(max_length=200, blank=True, null=True)
    club_type = models.IntegerField(blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'club_types'



# 동아리 모델 
class Clubs(models.Model):
    club_id = models.AutoField(primary_key=True)
    club_name = models.CharField(max_length=200, blank=True, null=True)
    club_desc = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    club_type = models.OneToOneField(ClubTypes, models.DO_NOTHING)
    club_img_url = models.CharField(max_length=500, blank=True, null=True) #활동사진
    club_logo_url = models.CharField(max_length=500, blank=True, null=True)
    established = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    end_day = models.DateTimeField()
    deadline = models.IntegerField()
    rank = models.IntegerField()
    sns_link = models.CharField(max_length=500, blank=True, null=True)
    form_link = models.CharField(max_length=500, blank=True, null=True)
    
    def D_day(self,now):
        return int((self.end_day - now).days)

    # class Meta:
    #     managed = False
    #     db_table = 'clubs'