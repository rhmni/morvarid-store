from django.urls import path

from store_favorite.views import add_favorite_product, delete_favorite_product

app_name = 'store_favorite'
urlpatterns = [
    path('add-favorite-product/<int:product_id>', add_favorite_product, name='add_favorite_product'),
    path('delete-favorite-product/<int:product_id>', delete_favorite_product, name='delete_favorite_product'),
]
