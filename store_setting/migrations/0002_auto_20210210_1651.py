# Generated by Django 3.1.5 on 2021-02-10 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_setting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('register_date', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='setting',
            name='copyright',
            field=models.CharField(max_length=100),
        ),
    ]
