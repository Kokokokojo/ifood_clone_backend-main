from rest_framework import serializers
from payments.models import Order



class OrderSerializer(serializers.ModelSerializer):

    # restaurant_name = serializers.ReadOnlyField(source='restaurant.name')

    class Meta:
        model = Order

        fields = [
            'id',
            'description',
            'price',
            'user',
            'created_at'
        ]

