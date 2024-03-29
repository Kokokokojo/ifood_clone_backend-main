from rest_framework.decorators import api_view, permission_classes
from django.db.models import Q
from rest_framework.response import Response 
from rest_framework import status
from addresses.serializer import AddressSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Address

# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_addresses(request):
    
    try:
        address_get = Address.objects.filter(Q(user=request.user) & Q(is_active=True))
    except Exception:
        return Response({'_address_error':'Error returning user addresses'}, status=status.HTTP_404_NOT_FOUND)

    serializer = AddressSerializer(instance=address_get, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)