from django.urls import path
from payments.views import test_payment

urlpatterns = [
    path('test-payment/', test_payment),
]

