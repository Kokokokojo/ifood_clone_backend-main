from django.contrib import admin
from restaurants.models import Restaurant

# Register your models here.


class restaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state', 'zip_code', 'number', 'is_active')
    list_filter = ('is_active',)



admin.site.register(Restaurant, restaurantAdmin)
