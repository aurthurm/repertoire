# Generated by Django 2.0.5 on 2018-06-03 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20180603_1646'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-date_received',)},
        ),
    ]
