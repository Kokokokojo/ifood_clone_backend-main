from rest_framework.decorators import api_view, permission_classes
from django.db.models import Q
from rest_framework.response import Response 
from rest_framework import status
from restaurants.serializer import RestaurantSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Restaurant
import decimal 
# Create your views here.



# Restaurants data go through here for creating
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def register_restaurant(request):

    price_formated = decimal.Decimal(request.data.get('delivery_fee').replace(',', '.'))
    request.data['delivery_fee'] = price_formated

    serializer = RestaurantSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    serializer.validated_data['manager'] = request.user
    serializer.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)
    


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_available_restaurants(request):
    
    restaurant_get = Restaurant.objects.filter(Q(manager=request.user) & Q(is_active=True))
    serializer = RestaurantSerializer(instance=restaurant_get, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def available_restaurants(request):
    restaurant_get = Restaurant.objects.filter(Q(is_active=True))
    serializer = RestaurantSerializer(instance=restaurant_get, many=True)


    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_restaurant(request, restaurant_id):

    restaurant_get = Restaurant.objects.get(Q(is_active=True) & Q(id=restaurant_id))
    serializer_restaurant = RestaurantSerializer(instance=restaurant_get, many=False)


    return Response(serializer_restaurant.data, status=status.HTTP_200_OK)



@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deactivate_restaurant(request, restaurant_id):

    restaurant_get = Restaurant.objects.get(Q(is_active=True) & Q(manager=request.user) & Q(id=restaurant_id))
    restaurant_get.is_active = False
    restaurant_get.save()

    return Response({'success':True}, status=status.HTTP_204_NO_CONTENT)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_restaurant(request):
    request.data._mutable=True

    restaurant_id = request.data['restaurant_id']

    price_formated = decimal.Decimal(request.data.get('delivery_fee').replace(',', '.'))
    request.data['delivery_fee'] = price_formated

    restaurant_get = Restaurant.objects.get(Q(is_active=True) & Q(manager=request.user) & Q(id=restaurant_id))

    serializer = RestaurantSerializer(instance=restaurant_get,
                                            data=request.data, 
                                            many=False,
                                            partial=True,)
    serializer.is_valid(raise_exception=True)
 
    serializer.save()

    return Response(serializer.data, status=status.HTTP_200_OK)