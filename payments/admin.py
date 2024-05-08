from django.contrib import admin
from payments.models import Order

# Register your models here.

class ordersAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'restaurant', 'price', 'cpf', 'cnpj', 'email', 'created_at',)
    list_filter = ('created_at',)




admin.site.register(Order, ordersAdmin)
