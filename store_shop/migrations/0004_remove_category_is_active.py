# Generated by Django 3.1.5 on 2021-02-04 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_shop', '0003_auto_20210204_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='is_active',
        ),
    ]
