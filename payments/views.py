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


def save_stripe_info(request):
    email = request.data['email']
    payment_method_id = request.data['payment_method_id']
    amount = int(request.data['amount'])
    extra_msg = 'New costumer added.'


    # checking if customer with provided email already exists
    customer_data = stripe.Customer.list(email=email).data   
     
    # if the array is empty it means the email has not been used yet  
    if len(customer_data) == 0:
        # creating customer
        customer = stripe.Customer.create(
        email=email, payment_method=payment_method_id)
    else:
        customer = customer_data[0]
        extra_msg = "Customer already existed."


    stripe.PaymentIntent.create(
        customer=customer, 
        payment_method=payment_method_id,  
        currency='brl', 
        amount=amount,
        confirm=True,
    )     


    return Response(status=status.HTTP_200_OK, 
        data={'message': 'Success', 'data': {'customer_id': customer.id}, 'extra_msg':extra_msg}
    )    