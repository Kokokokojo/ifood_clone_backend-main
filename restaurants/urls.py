from django.urls import path
from restaurants.views import register_restaurant

# CRIAR ROTA user-available-restaurants, ver a products ou users de exemplo

urlpatterns = [
    path('register-restaurant/', register_restaurant, name='register-restaurant'),
]

