# Generated by Django 4.0.2 on 2022-02-19 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_remove_product_sub_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.CharField(default='', max_length=50),
        ),
    ]