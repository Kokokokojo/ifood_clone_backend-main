from rest_framework.decorators import api_view, permission_classes
from django.db.models import Q
from rest_framework.response import Response 
from rest_framework import status
from restaurants.serializer import RestaurantSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Restaurant
from categories.models import Category
import decimal 
from rest_framework.pagination import PageNumberPagination


# Create your views here.




class RestaurantsPagination(PageNumberPagination):

    page_size = 20

    def get_paginated_response(self, data):
        return Response({
            'page_size': self.page_size,
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page_number': self.page.number,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })




# Restaurants data go through here for creating
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def register_restaurant(request):
    request.data._mutable=True

    price_formated = decimal.Decimal(request.data.get('delivery_fee').replace(',', '.'))
    request.data['delivery_fee'] = price_formated
    request.data['partner_delivery'] = True if request.data.get('partner_delivery') == 'True' else False

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
def available_restaurants_search(request):
    
    super_restaurant = False if request.query_params.get('super_restaurant','') == 'false' else True
    free_delivery = False if request.query_params.get('free_delivery','') == 'false' else True
    partner_delivery = False if request.query_params.get('partner_delivery','') == 'false' else True
    
    category_id = request.query_params.get('category_id','')
    order_by = request.query_params.get('order_by').strip() if request.query_params.get('order_by').strip() else 'id'


    query = Q()
    paginator = RestaurantsPagination()


    if super_restaurant is True:
        query &= Q(super_restaurant = True)

    else:
        # IF I WANT TO NEGATE THE QUERY
        # query &= ~Q(super_restaurant=True)
        pass


    if free_delivery is True:
        query &= Q(delivery_fee = 0)


    if partner_delivery is True:
        query &= Q(partner_delivery = True)


    if category_id:
        try:
            id_cat = int(category_id)
            category = Category.objects.get(Q(id=id_cat) & Q(is_active=True))
            query &= Q(category = category)

        except Category.DoesNotExist:
            pass


    restaurant_get = Restaurant.objects.filter(Q(is_active=True) & query).order_by(f'{"" if order_by == "id" else "-"}{order_by}')


    result_page = paginator.paginate_queryset(restaurant_get, request)
    serializer = RestaurantSerializer(result_page, many=True)

    return paginator.get_paginated_response(serializer.data)



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
@parser_classes([MultiPartParser, FormParser])
def update_restaurant(request):
    request.data._mutable=True

    restaurant_id = request.data['restaurant_id']

    price_formated = decimal.Decimal(request.data.get('delivery_fee').replace(',', '.'))
    request.data['delivery_fee'] = price_formated
    request.data['partner_delivery'] = True if request.data.get('partner_delivery').capitalize() == 'True' else False

    restaurant_get = Restaurant.objects.get(Q(is_active=True) & Q(manager=request.user) & Q(id=restaurant_id))

    serializer = RestaurantSerializer(instance=restaurant_get,
                                            data=request.data, 
                                            many=False,
                                            partial=True,)
    serializer.is_valid(raise_exception=True)
 
    serializer.save()

    return Response(serializer.data, status=status.HTTP_200_OK)