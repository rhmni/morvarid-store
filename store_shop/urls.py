from django.urls import path

from .views import ProductDetail, product_list

app_name = 'store_shop'
urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('products/<slug:category>/', product_list, name='product_list_category'),
    path('products/<int:product_id>/<title>', ProductDetail.as_view(), name='product_detail'),
]
