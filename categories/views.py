from rest_framework.decorators import api_view, permission_classes
from django.db.models import Q
from rest_framework.response import Response 
from rest_framework import status
from .models import Category
from .serializer import CategorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def available_categories(request):
    
    categories_get = Category.objects.filter(is_active=True)

    serializer = CategorySerializer(instance=categories_get, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)