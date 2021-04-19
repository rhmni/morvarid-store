from django.db import models

from store_shop.models import Product
from store_user.models import User


class FavoriteRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favoriteproducts')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favoriteuser')
    register_date = models.DateTimeField()

    def __str__(self):
        return f'{self.user} / {self.product}'

    class Meta:
        ordering = ('-register_date',)

