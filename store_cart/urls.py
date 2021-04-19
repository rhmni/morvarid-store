from django.urls import path

from store_cart.views import cart_detail, add_cart_item, delete_cart_item, cart_history, invoice_detail, pay_cart

app_name = 'store_cart'

urlpatterns = [
    path('cart-detail', cart_detail, name='cart_detail'),
    path('add-cart-item/<int:product_id>', add_cart_item, name='add_cart_item'),
    path('delete-cart-item/<int:product_id>', delete_cart_item, name='delete_cart_item'),
    path('cart-history', cart_history, name='cart_history'),
    path('invoice-detail/<int:cart_id>', invoice_detail, name='invoice_detail'),
    path('pay_cart', pay_cart, name='pay_cart'),
]
