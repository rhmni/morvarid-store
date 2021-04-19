from django.db import models


class Setting(models.Model):
    site_title = models.CharField(max_length=50)
    site_description = models.CharField(max_length=50)
    newsletter_title = models.CharField(max_length=50)
    newsletter_description = models.CharField(max_length=50)
    about_us = models.TextField()
    copyright = models.CharField(max_length=100)
    mobile = models.PositiveBigIntegerField()
    telegram = models.CharField(max_length=150)
    instagram = models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.site_title


class Newsletter(models.Model):
    email = models.CharField(max_length=100)
    register_date = models.DateTimeField()

    def __str__(self):
        return self.email
