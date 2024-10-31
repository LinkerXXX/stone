from django.contrib import admin
from user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    listdisplay = ('registration_date','first_name','last_name','email','avatar')
    ordering = [ 'registration_date','avatar']