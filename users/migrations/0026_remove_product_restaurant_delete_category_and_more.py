# Generated by Django 4.2.1 on 2024-03-13 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_restaurant_address_zip_code_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='restaurant',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Restaurant',
        ),
    ]
