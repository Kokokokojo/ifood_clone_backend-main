from django.urls import path
from .views import register_product, available_products, get_product, update_product


urlpatterns = [
    path('register-product/', register_product, name='register-product'),
    path('available-products/', available_products, name='available-products'),
    path('get/<int:product_id>/', get_product, name='get-product'),
    path('update-product/', update_product, name='update-restaurant'),
]
