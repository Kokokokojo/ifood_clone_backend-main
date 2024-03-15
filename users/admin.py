from django.contrib import admin

# Register your models here.
from django.contrib import admin
from users.models import CustomUser


class userAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'is_active', 'is_staff')
    list_filter = ( 'is_active', 'is_staff')



admin.site.register(CustomUser, userAdmin)
