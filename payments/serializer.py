from rest_framework import serializers
from payments.models import Order



class OrderSerializer(serializers.ModelSerializer):

    # restaurant_name = serializers.ReadOnlyField(source='restaurant.name')
    # avg_order_price = serializers.SerializerMethodField()
    avg_order_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Order

        fields = [
            'id',
            'description',
            'price',
            'user',
            'created_at',
            'avg_order_price',
            'type',
        ]

    # def get_avg_order_price(self, obj):
    #     items = obj.items.all()  
    #     total_price = sum(item.price for item in items)

    #     if items:
    #         avg_order_price = total_price / len(items)
    #     else:
    #         avg_order_price = 0  # Default value if there are no items in the order

    #     return avg_order_price

