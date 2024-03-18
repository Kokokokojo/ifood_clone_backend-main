from rest_framework.decorators import api_view, permission_classes
from django.db.models import Q
from rest_framework.response import Response 
from rest_framework import status
from restaurants.serializer import RestaurantSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.



# Restaurants data go through here
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def register_restaurant(request):

    serializer =  RestaurantSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)
    