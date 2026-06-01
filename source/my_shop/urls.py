from django.urls import path
from my_shop.views import products_view,add_category, add_product, product_detail

urlpatterns = [
    path('products/', products_view, name='products'),
    path('categories/add/', add_category, name='add_category'),
    path('products/add/', add_product, name='add_product'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
]