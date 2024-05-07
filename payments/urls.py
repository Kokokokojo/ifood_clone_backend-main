from django.urls import path
from payments.views import save_stripe_info

urlpatterns = [
    path('save-stripe-info/', save_stripe_info),
]

