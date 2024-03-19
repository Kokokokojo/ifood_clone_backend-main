from rest_framework.decorators import api_view, permission_classes
from django.db.models import Q
from rest_framework.response import Response 
from rest_framework import status
from products.models import Product, Category
from restaurants.models import Restaurant
from .serializer import ProductSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
import decimal 
from copy import deepcopy
import json

# Create your views here.



# TUDO isso para o upload de Imagem
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def register_product(request):

    restaurant_id = request.data.get('restaurant_id', -1)

    try:
        restaurant = Restaurant.objects.get(id = restaurant_id)

    except Restaurant.DoesNotExist:

        return Response({'restaurant_does_not_exist':'Restaurante inexistente'}, status=status.HTTP_404_NOT_FOUND)
    

    price_formated = decimal.Decimal(request.data.get('price').replace(',', '.'))
    request.data['price'] = price_formated
    request.data['restaurant'] = restaurant_id


    serializer =  ProductSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    product = serializer.save()

    categories_decoded = json.loads(request.data['categories'])

    categories_ids = []

    for categories in categories_decoded:
        for key, val in categories.items():
            if key == 'id':
                categories_ids.append(int(val))


    product.categories.add(*categories_ids) 


    return Response(serializer.data, status=status.HTTP_201_CREATED)
    



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def available_categories(request):
    
    categories_get = Category.objects.filter(is_active=True)



    serializer = CategorySerializer(instance=categories_get, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)