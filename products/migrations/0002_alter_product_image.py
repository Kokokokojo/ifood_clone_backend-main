# Generated by Django 4.2.1 on 2024-03-18 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/logos/%Y/%m/%d'),
        ),
    ]
