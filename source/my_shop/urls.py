from django.urls import path
from my_shop.views import products_view,add_category, add_product

urlpatterns = [
    path('products/', products_view, name='products'),
    # path('products/<int:pk>/', products_view, name='product'),
    path('categories/add/', add_category, name='add_category'),
    path('products/add/', add_product, name='add_product'),
]