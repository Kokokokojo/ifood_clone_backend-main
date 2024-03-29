from django.urls import path
from .views import user_addresses


urlpatterns = [
    path('user-addresses/', user_addresses, name='user-addresses'),
]
