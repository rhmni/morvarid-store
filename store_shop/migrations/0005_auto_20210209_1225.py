# Generated by Django 3.1.5 on 2021-02-09 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_shop', '0004_remove_category_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-id',)},
        ),
    ]