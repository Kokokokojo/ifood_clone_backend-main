from rest_framework import serializers
from products.models import Product, Category


class CategorySerializer(serializers.ModelSerializer):    

    class Meta:
        model = Category

        fields = [
            'id',
            'name',
            'description',
        ]

        


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


