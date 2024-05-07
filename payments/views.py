from rest_framework.decorators import api_view
from django.db.models import Q
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
import stripe
from dotenv import load_dotenv
import os 
# Create your views here.
load_dotenv()
stripe.api_key = os.environ.get('stripe_secret_key')

@api_view(['POST'])
def test_payment(request):

    test_payment_intent = stripe.PaymentIntent.create(
    amount=1000, currency='pln', 
    payment_method_types=['card'],
    receipt_email='test@example.com')

    return Response(status=status.HTTP_200_OK, data=test_payment_intent)