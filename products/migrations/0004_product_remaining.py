# Generated by Django 2.0.5 on 2018-06-03 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_product_remaining'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='remaining',
            field=models.IntegerField(default=0),
        ),
    ]
