from django.urls import path
from restaurants.views import( register_restaurant, user_available_restaurants, 
                              available_restaurants, available_restaurants_search, deactivate_restaurant, update_restaurant, get_restaurant)

# CRIAR ROTA user-available-restaurants, ver a products ou users de exemplo

urlpatterns = [
    path('register-restaurant/', register_restaurant, name='register-restaurant'),
    path('user-available-restaurants/', user_available_restaurants, name='user-available-restaurant'),
    path('available-restaurants/', available_restaurants, name='available-restaurant'),
    path('available-restaurants-search/', available_restaurants_search, name='available-restaurant-search'),
    path('<int:restaurant_id>/', deactivate_restaurant, name='deactivate-restaurant'),
    path('get/<int:restaurant_id>/', get_restaurant, name='get-restaurant'),
    path('update-restaurant/', update_restaurant, name='update-restaurant'),
]

