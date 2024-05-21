from rest_framework import serializers
from products.models import Product
from categories.serializer import CategorySerializer



class ProductSerializer(serializers.ModelSerializer):

    restaurant_name = serializers.ReadOnlyField(source='restaurant.name')
    restaurant_state = serializers.ReadOnlyField(source='restaurant.state')
    restaurant_id = serializers.ReadOnlyField(source='restaurant.id')
    restaurant_delivery_fee = serializers.ReadOnlyField(source='restaurant.delivery_fee')
    categories = CategorySerializer(read_only=True, many=True)

    class Meta:
        model = Product

        fields = [
            'id',
            'name',
            'description',
            'price',
            'total_sales',
            'image',
            'restaurant_name',
            'restaurant_address',
            'restaurant_id',
            'restaurant_state',
            'restaurant_delivery_fee',
            'restaurant',
            'categories',
        ]

