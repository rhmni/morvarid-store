from django.db import models

from store_shop.models import Product
from store_user.models import User


class Comment(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usercomments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='postcomments')
    reply = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replycomments', null=True, blank=True)
    text = models.TextField()
    is_reply = models.BooleanField(default=False)
    created_date = models.DateTimeField()

    def __str__(self):
        return f'{self.writer.email} / {self.text[:10]}'

    class Meta:
        ordering = ('-created_date',)
