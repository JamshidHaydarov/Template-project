# Generated by Django 5.0.3 on 2024-04-07 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteapp', '0002_cart_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.IntegerField(default=1),
        ),
    ]
