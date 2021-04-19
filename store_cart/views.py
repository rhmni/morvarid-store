from datetime import datetime

from django.contrib import messages
from django.http import Http404

from store_setting.models import Setting
from store_user.models import User
from .forms import AddCartItemForm, AddCouponForm
from .models import Cart, CartItem, Coupon
from store_shop.models import Product
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


@login_required
def cart_detail(request):
    try:
        cart = Cart.objects.get(user=request.user, is_paid=False)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=request.user, create_date=datetime.now())
    cart.discount = 0
    cart.save()

    cart_items = CartItem.objects.filter(
        cart__user=request.user,
        cart__is_paid=False,
        product__is_active=True,
        product__is_available=True
    )
    for item in cart_items:
        item.price = item.product.price
        item.save()

    if request.method == 'POST':
        coupon_form = AddCouponForm(request.POST)
        if coupon_form.is_valid():
            try:
                coupon = Coupon.objects.get(code=coupon_form.cleaned_data['code'], is_active=True,
                                            valid_from__lt=datetime.now(), valid_to__gt=datetime.now())
                cart.discount = (coupon.discount / 100) * cart.final_price
                cart.save()
                messages.success(request, 'کد تخفیف با موفقیت ثبت شد', 'success')
            except Coupon.DoesNotExist:
                messages.success(request, 'این کد تخفیف معتبر نمی باشد', 'error')
    else:
        coupon_form = AddCouponForm()

    context = {
        'title': 'سبد خرید',
        'cart_items': cart_items,
        'cart': cart,
        'coupon_form': coupon_form,
    }
    return render(request, 'store_cart/cart_detail.html', context)


@login_required
@require_POST
def add_cart_item(request, product_id):
    product = get_object_or_404(Product, id=product_id, is_active=True, is_available=True)
    try:
        cart = Cart.objects.get(user=request.user, is_paid=False)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=request.user, create_date=datetime.now())
    form = AddCartItemForm(request.POST)
    if form.is_valid():
        quantity = form.cleaned_data['qtyinput']
        try:
            cart_item = cart.cartitems.get(product=product)
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, 'این محصول به سبد خرید شما اضافه شد', 'success')
            cart.update_date = datetime.now()
            cart.save()

        except CartItem.DoesNotExist:
            cart.cartitems.create(product=product, price=product.price, quantity=quantity, create_date=datetime.now())
            messages.success(request, 'این محصول به سبد خرید شما اضافه شد', 'success')
            cart.update_date = datetime.now()
            cart.save()

    return redirect('store_shop:product_detail', product.id, product.title.replace(' ', '-'))


@login_required
def delete_cart_item(request, product_id):
    product = get_object_or_404(Product, id=product_id, is_active=True, is_available=True)
    get_object_or_404(CartItem, product=product, cart__user=request.user, cart__is_paid=False).delete()
    cart = Cart.objects.get(user=request.user, is_paid=False)
    cart.update_date = datetime.now()
    cart.save()
    messages.success(request, 'این محصول از سبد خرید شما حذف شد', 'success')
    return redirect('store_cart:cart_detail')


@login_required
def cart_history(request):
    carts = Cart.objects.filter(user=request.user, is_paid=True)
    context = {
        'title': 'صورتحساب های قبلی',
        'carts': carts,
    }
    return render(request, 'store_cart/cart_history.html', context)


@login_required
def invoice_detail(request, cart_id):
    cart = get_object_or_404(Cart, user=request.user, is_paid=True, id=cart_id)
    if request.user == cart.user:
        setting = Setting.objects.last()
        context = {
            'cart': cart,
            'setting': setting,
        }
        return render(request, 'store_cart/invoice_detail.html', context)
    else:
        raise Http404


@login_required
def pay_cart(request):
    user = User.objects.get(id=request.user.id)
    if user.phone and user.code_meli and user.ostan and user.shahr and user.address:
        cart = get_object_or_404(Cart, user=user, is_paid=False)
        cart.is_paid = True
        cart.pay_date = datetime.now()
        cart.save()
        messages.success(request, 'سفارش شما پرداخت شد', 'success')
        return redirect('store_main:home')
    else:
        messages.success(request, 'پروفایل شما ناقص است ابتدا آن را کامل کنید', 'error')
        return redirect('store_cart:cart_detail')
