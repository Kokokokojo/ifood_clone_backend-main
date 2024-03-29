from django.urls import path
from .views import register_product, available_products, get_product, update_product, delete_product, available_products_restaurant


urlpatterns = [
    path('register-product/', register_product, name='register-product'),
    path('available-products/', available_products, name='available-products'),
    path('available-products-restaurant/<int:id_restaurant>/', available_products_restaurant, name='available-products-restaurant'),

    path('get/<int:product_id>/', get_product, name='get-product'),
    path('update-product/', update_product, name='update-restaurant'),
    path('delete-product/<int:product_id>/', delete_product, name= 'delete-product'),
]
