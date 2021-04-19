from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from store_favorite.models import FavoriteRelation
from store_shop.models import Product


@login_required
def add_favorite_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    FavoriteRelation.objects.create(user=request.user, product=product, register_date=datetime.now())
    messages.success(request, f'{product.title} به محصولات مورد علاقه شما اضافه شد', 'success')
    return redirect('store_shop:product_detail', product_id, product.title.replace(' ', '-'))


@login_required
def delete_favorite_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    FavoriteRelation.objects.filter(user=request.user, product=product).delete()
    messages.success(request, f'{product.title} از محصولات مورد علاقه شما حذف شد', 'success')
    return redirect('store_shop:product_detail', product_id, product.title.replace(' ', '-'))
