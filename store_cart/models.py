from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from store_shop.models import Product
from store_user.models import User


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    is_paid = models.BooleanField(default=False)
    discount = models.PositiveIntegerField(null=True, blank=True, default=0)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField(null=True, blank=True)
    pay_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ('-create_date',)

    @property
    def total_price(self):
        total = 0
        for cart_item in self.cartitems.all():
            total += (cart_item.price * cart_item.quantity)
        return int(total)

    @property
    def final_price(self):
        total = 0
        for cart_item in self.cartitems.all():
            total += (cart_item.price * cart_item.quantity)
        return int(total) - int(self.discount)

    def __str__(self):
        return f'{self.user.email} -- {self.create_date.year} / {self.create_date.month} / {self.create_date.day}'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartitems')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='productitem')
    price = models.PositiveIntegerField()
    quantity = models.PositiveSmallIntegerField()
    create_date = models.DateTimeField()

    @property
    def total_price(self):
        return int(self.price * self.quantity)

    def __str__(self):
        return self.product.title


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], help_text='percent')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.code
