from django.urls import path
from payments.views import save_stripe_info, mark_order_cancelled_tk, mark_order_done_tk, mark_order_ready_tk

urlpatterns = [
    path('save-stripe-info/', save_stripe_info),

    path('mark-order-ready-tk/', mark_order_ready_tk),
    path('mark-order-done-tk/', mark_order_done_tk),
    path('mark-order-cancelled-tk/', mark_order_cancelled_tk),

]

