from django.db import models

from store_user.models import User


class Ticket(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fromusertickets')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tousertickets', null=True, blank=True)
    text = models.TextField(max_length=400)
    send_date = models.DateTimeField()

    def __str__(self):
        return f'{self.from_user} - {self.text[:20]}'

    class Meta:
        ordering = ('id',)
