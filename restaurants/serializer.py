from rest_framework import serializers
from restaurants.models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):

    category_name = serializers.CharField(source='category.name', required=False)
    manager_id = serializers.CharField(source='manager.id', required=False)

    class Meta:
        model = Restaurant

        fields = [
            'id',
            'name',
            'description',
            'logo',
            'banner',
            'street',
            'complement',
            'reference_point',
            'neighborhood',
            'number',
            'city',
            'state',
            'zip_code',
            'cnpj',
            'delivery_fee',
            'super_restaurant',
            'partner_delivery',
            'manager',
            'category_name',
            'manager_id',
        ]



