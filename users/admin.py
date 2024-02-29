from django.contrib import admin

# Register your models here.
from django.contrib import admin
from users.models import CustomUser, Address


class userAdmin(admin.ModelAdmin):
    pass

class addressAdmin(admin.ModelAdmin):
    pass

admin.site.register(CustomUser, userAdmin)
admin.site.register(Address, addressAdmin)
