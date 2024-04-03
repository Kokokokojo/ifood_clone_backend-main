from rest_framework import serializers
from restaurants.models import Restaurant, RestaurantRating
from django.db.models import Avg






class RestaurantSerializer(serializers.ModelSerializer):
        

    category_name = serializers.CharField(source='category.name', required=False)
    manager_id = serializers.CharField(source='manager.id', required=False)
    restaurant_avg_rating = serializers.SerializerMethodField()



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
            'restaurant_avg_rating',
            'super_restaurant',
            'partner_delivery',
            'manager',
            'category_name',
            'manager_id',
        ]


    def get_restaurant_avg_rating(self, obj):
        average_rating = RestaurantRating.objects.filter(restaurant=obj).aggregate(restaurant_avg_rating=Avg('rating'))['restaurant_avg_rating']
        
        formatted_rating = "{:.1f}".format(average_rating)

        return formatted_rating



