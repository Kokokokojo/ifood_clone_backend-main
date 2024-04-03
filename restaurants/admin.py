from django.contrib import admin
from restaurants.models import Restaurant, RestaurantRating

# Register your models here.


class restaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state', 'zip_code', 'number', 'is_active',)
    list_filter = ('is_active', 'state',)


class restaurantRatingAdmin(admin.ModelAdmin):
    list_display = ('rating', 'restaurant',)
    list_filter = ('rating',)



admin.site.register(Restaurant, restaurantAdmin)
admin.site.register(RestaurantRating, restaurantRatingAdmin)
