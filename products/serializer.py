from rest_framework import serializers
from products.models import Product
from categories.serializer import CategorySerializer



class ProductSerializer(serializers.ModelSerializer):

    restaurant_name = serializers.ReadOnlyField(source='restaurant.name')
    
    categories = CategorySerializer(read_only=True, many=True)

    class Meta:
        model = Product

        fields = [
            'id',
            'name',
            'description',
            'price',
            'qtd',
            'image',
            'restaurant_name',
            'restaurant',
            'categories',
        ]


