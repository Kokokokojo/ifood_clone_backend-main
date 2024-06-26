from django.urls import path
from .views import user_addresses, select_active_address, register_address, deactivate_Address


urlpatterns = [
    path('user-addresses/', user_addresses, name='user-addresses'),
    path('select-active/', select_active_address, name='select_active_address'),
    path('register-user-address/', register_address, name='register-user-address'),
    path('<int:address_id>/', deactivate_Address, name='deactivate-address'),

]
