from rest_framework.decorators import api_view, permission_classes
from django.db.models import Q
from rest_framework.response import Response 
from rest_framework import status
from restaurants.models import Restaurant
from products.models import Product
from .serializer import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
import decimal 
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
def available_products(request):

    product_get = Product.objects.filter(Q(is_active=True))[:25]
    serializer = ProductSerializer(instance=product_get, many=True)


    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def available_products_restaurant(request, id_restaurant):

    search = request.query_params.get('q','') 
    query = Q()

    if search:
        query &= Q(name__icontains = search)
        print(query)
        print(search)
    
    product_get = Product.objects.filter(Q(is_active=True) & Q(restaurant = id_restaurant) & Q(name__icontains = search))


    serializer = ProductSerializer(instance=product_get, many=True)


    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_product(request, product_id):
    product_get = Product.objects.get(Q(is_active=True) & Q(id=product_id))

    serializer = ProductSerializer(instance=product_get, many=False)

    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def update_product(request):
    request.data._mutable=True

    restaurant_id = request.data.get('restaurant_id', -1)
    product_id = request.data.get('id', -1)

    try:
        restaurant = Restaurant.objects.get(Q(id = restaurant_id) & Q(manager=request.user))
    
        product = Product.objects.get(Q(id = product_id))

    except Restaurant.DoesNotExist:

        return Response({'restaurant_does_not_exist':'Restaurante inexistente'}, status=status.HTTP_404_NOT_FOUND)
    
    except Product.DoesNotExist:

        return Response({'product_does_not_exist':'Produto inexistente'}, status=status.HTTP_404_NOT_FOUND)
    

    price_formated = decimal.Decimal(request.data.get('price').replace(',', '.'))
    request.data['price'] = price_formated
    request.data['restaurant'] = restaurant_id


    serializer = ProductSerializer(instance=product,
                                        data=request.data, 
                                        many=False,
                                        partial=True,)
    serializer.is_valid(raise_exception=True)

    product = serializer.save()

    categories_decoded = json.loads(request.data['categories'])

    categories_ids = []

    for categories in categories_decoded:
        for key, val in categories.items():
            if key == 'id':
                categories_ids.append(int(val))


    product.categories.add(*categories_ids) 


    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_product(request, product_id):

    product_get = Product.objects.get(Q(is_active=True) & Q(id=product_id))
    product_get.is_active = False
    product_get.save()  

    return Response({'success':True}, status=status.HTTP_204_NO_CONTENT)