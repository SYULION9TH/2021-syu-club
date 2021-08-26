from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(AuthUser)
admin.site.register(ClubTypes)
admin.site.register(Clubs)
admin.site.register(Posts)