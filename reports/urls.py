from django.urls import path
from reports.views import top_selling_restaurants, sales_performance_by_product_category, sales_performance_product

urlpatterns = [
    path('top-selling-restaurants/', top_selling_restaurants, name='filter-data-charts-top-selling-restaurants'),
    path('sales-performance-by-product-category/', sales_performance_by_product_category, name='filter-data-charts-category-performance'),
    path('sales-product/', sales_performance_product, name='filter-data-charts-product-performance'),
]
