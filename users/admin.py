from django.contrib import admin

# Register your models here.
from django.contrib import admin
from users.models import CustomUser, Address


class userAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'is_active', 'is_staff')
    list_filter = ( 'is_active', 'is_staff')

class addressAdmin(admin.ModelAdmin):
    list_display = ('name', 'street', 'zip_code', 'city', 'state', 'is_active', 'user')
    list_filter = ('name', 'city', 'zip_code', 'state', 'is_active', 'user')



admin.site.register(CustomUser, userAdmin)
admin.site.register(Address, addressAdmin)
