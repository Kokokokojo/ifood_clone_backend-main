from rest_framework import serializers
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):

    restaurant_name = serializers.ReadOnlyField(source='restaurant.name')

    class Meta:
        model = Product

        fields = [
            'id',
            'name',
            'description',
            'price',
            'qtd',
            'image',
            'restaurant_name'
        ]

        