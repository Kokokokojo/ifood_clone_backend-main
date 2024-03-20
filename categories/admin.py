from django.contrib import admin
from .models import Category

# Register your models here.


class categoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_active')
    list_filter = ('is_active',)


admin.site.register(Category, categoryAdmin)
