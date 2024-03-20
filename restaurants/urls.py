from django.urls import path
from restaurants.views import register_restaurant, user_available_restaurants, available_restaurants, deactivate_restaurant

# CRIAR ROTA user-available-restaurants, ver a products ou users de exemplo

urlpatterns = [
    path('register-restaurant/', register_restaurant, name='register-restaurant'),
    path('user-available-restaurants/', user_available_restaurants, name='user-available-restaurant'),
    path('available-restaurants/', available_restaurants, name='available-restaurant'),
    path('<int:restaurant_id>/', deactivate_restaurant, name='deactivate-restaurant'),

]

