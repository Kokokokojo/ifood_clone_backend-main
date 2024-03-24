# Generated by Django 4.2.1 on 2024-03-19 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_restaurant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(blank=True, to='products.category'),
        ),
    ]