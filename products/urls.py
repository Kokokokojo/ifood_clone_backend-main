from django.urls import path
from .views import register_product, available_categories


urlpatterns = [
    path('register-product/', register_product, name='register-product'),
    path('available-categories/', available_categories, name='available-categories'),

]
