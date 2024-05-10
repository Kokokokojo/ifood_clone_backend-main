from django.urls import path
from reports.views import avg_price_over_time, sales_performance_by_product_category, sales_performance_product

urlpatterns = [
    path('avg-price-over-time/', avg_price_over_time, name='filter-data-charts-price-over-time'),
    path('sales-performance-by-product-category/', sales_performance_by_product_category, name='filter-data-charts-category-performance'),
    path('sales-product/', sales_performance_product, name='filter-data-charts-product-performance'),
]
