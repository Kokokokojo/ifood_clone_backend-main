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
            'street',
            'complement',
            'neighborhood',
            'number',
            'city',
            'state',
            'zip_code',
            'cnpj',
            'delivery_fee',
            'super_restaurant',
            'manager',
            'category_name',
            'manager_id',
        ]



