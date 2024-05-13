from rest_framework import serializers

# just a helper
class CategorySalesSerializer(serializers.Serializer):
    categories__name = serializers.CharField()
    total_sales = serializers.DecimalField(max_digits=10, decimal_places=2)


class ProductSalesSerializer(serializers.Serializer):
    name = serializers.CharField()
    total_sales = serializers.DecimalField(max_digits=10, decimal_places=2)
    price = serializers.DecimalField(max_digits=7, decimal_places=2)

