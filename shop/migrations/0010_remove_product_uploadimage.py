# Generated by Django 4.0.2 on 2022-02-19 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_product_uploadimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='uploadimage',
        ),
    ]
