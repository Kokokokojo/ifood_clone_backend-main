from rest_framework.decorators import api_view, permission_classes
from django.db.models import Q
from rest_framework.response import Response 
from rest_framework import status
from products.models import Product, Category
from restaurants.models import Restaurant
from .serializer import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
import decimal 
from copy import deepcopy

# Create your views here.



# TUDO isso para o upload de Imagem
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def register_product(request):

    restaurant_id = request.data.get('restaurant_id', '')

    try:
        restaurant = Restaurant.objects.get(id = restaurant_id)

    except Restaurant.DoesNotExist:

        return Response({'restaurant_does_not_exist':'Restaurante inexistente'}, status=status.HTTP_404_NOT_FOUND)

    price_formated = decimal.Decimal(request.data.get('price').replace(',', '.'))
    request.data['price'] = price_formated


    serializer =  ProductSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    serializer.validated_data['restaurant'] = restaurant
    serializer.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)
    

    # return Response(serializer.data, status=status.HTTP_201_CREATED)