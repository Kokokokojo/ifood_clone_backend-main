from rest_framework.decorators import api_view, permission_classes
from django.db.models import Q, Sum
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from payments.models import Order
from payments.serializer import OrderSerializer
from products.serializer import  Product
from .serializer import CategorySalesSerializer, ProductSalesSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def avg_price_over_time(request):
    startDate = request.query_params.get('startDate', '')
    endDate = request.query_params.get('endDate', '')

    query = Q()

    try:
        if startDate:
            parsed_start_date = datetime.strptime(startDate, "%Y-%m-%dT%H:%M").strftime('%Y-%m-%d %H:%M')
            query &= Q(created_at__gte=parsed_start_date)
        if endDate:
            parsed_end_date = datetime.strptime(endDate, "%Y-%m-%dT%H:%M").strftime('%Y-%m-%d %H:%M')
            query &= Q(created_at__lte=parsed_end_date)
    except ValueError:
        return Response({'error': 'Invalid date format'}, status=status.HTTP_400_BAD_REQUEST)


    orders_within_range = Order.objects.filter(query)
    order_serialized = OrderSerializer(instance=orders_within_range, many=True)
    return Response({'data': order_serialized.data}, status=status.HTTP_200_OK)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def sales_performance_by_product_category(request):
    startDate = request.query_params.get('startDate', '')
    endDate = request.query_params.get('endDate', '')

    query = Q()

    try:
        if startDate:
            parsed_start_date = datetime.strptime(startDate, "%Y-%m-%dT%H:%M").strftime('%Y-%m-%d %H:%M')
            query &= Q(created_at__gte=parsed_start_date)
        if endDate:
            parsed_end_date = datetime.strptime(endDate, "%Y-%m-%dT%H:%M").strftime('%Y-%m-%d %H:%M')
            query &= Q(created_at__lte=parsed_end_date)

        """
            This is the query if product had a foreign key category instead of a many to many categories
            category_sales = (
            Product.objects
            .filter(query)  # Filter products based on orders within the date range
            .values('category__name')  # Group by category name
            .annotate(total_sales=Sum('total_sales'))  # Calculate total sales for each category
        )
        """
        # Calculate total sales by category for the specified date range
        category_sales = (
            Product.objects
            .filter(query)  # Filter products based on orders within the date range
            .prefetch_related('categories')  # Prefetch categories to avoid N+1 queries
            .values('categories__name')  # Group by category name
            .annotate(total_sales=Sum('total_sales'))  # Calculate total sales for each category
        )

        serializer = CategorySalesSerializer(category_sales, many=True)

        return Response({'data':serializer.data}, status=status.HTTP_200_OK)


    except ValueError:
        return Response({'error': 'Invalid date format'}, status=status.HTTP_400_BAD_REQUEST)






@api_view(['GET'])
@permission_classes([IsAuthenticated])
def sales_performance_product(request):
    startDate = request.query_params.get('startDate', '')
    endDate = request.query_params.get('endDate', '')
    topNum = request.query_params.get('topNum', '')

    query = Q()

    try:
        if startDate:
            parsed_start_date = datetime.strptime(startDate, "%Y-%m-%dT%H:%M").strftime('%Y-%m-%d %H:%M')
            query &= Q(created_at__gte=parsed_start_date)
        if endDate:
            parsed_end_date = datetime.strptime(endDate, "%Y-%m-%dT%H:%M").strftime('%Y-%m-%d %H:%M')
            query &= Q(created_at__lte=parsed_end_date)
    except ValueError:
        return Response({'error': 'Invalid date format'}, status=status.HTTP_400_BAD_REQUEST)


    top_products = Product.objects.filter(query).order_by('-total_sales')
    serializer = ProductSalesSerializer(top_products, many=True)

    return Response({'data': serializer.data[:int(topNum)]}, status=status.HTTP_200_OK)

    
 