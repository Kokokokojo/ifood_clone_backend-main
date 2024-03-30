from django.contrib import admin

from .models import Address

# Register your models here.

class addressAdmin(admin.ModelAdmin):
    list_display = ('name', 'street', 'zip_code', 'city', 'state','is_selected', 'is_active', 'user')
    list_filter = ('name', 'city', 'zip_code', 'state', 'is_active', 'user')



admin.site.register(Address, addressAdmin)
