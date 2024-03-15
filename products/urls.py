from django.urls import path
from .views import register_product


urlpatterns = [
    path('register-product/', register_product, name='register-product'),
]
