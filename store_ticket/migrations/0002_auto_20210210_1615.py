# Generated by Django 3.1.5 on 2021-02-10 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_ticket', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'ordering': ('id',)},
        ),
    ]
