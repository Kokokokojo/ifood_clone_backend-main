from django.contrib import admin
from products.models import Product, Category

# Register your models here.


class productAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'restaurant', 'is_active')
    list_filter = ('is_active',)



admin.site.register(Product, productAdmin)


class categoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_active')
    list_filter = ('is_active',)



admin.site.register(Category, categoryAdmin)
