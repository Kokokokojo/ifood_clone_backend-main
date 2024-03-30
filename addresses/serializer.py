from rest_framework import serializers
from addresses.models import Address

class AddressSerializer(serializers.ModelSerializer):

    user_name= serializers.CharField(source='user.first_name', required=False, read_only=True)

    class Meta:
        model = Address

        fields = [
            'name',
            'street',
            'neighborhood',
            'number',
            'complement',
            'city',
            'state',
            'zip_code',
            'user',
            'user_name',
            'is_active' ,
            'is_selected',
            'type_of',
        ]



