# Generated by Django 4.2.1 on 2024-05-10 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_product_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='qtd',
        ),
        migrations.AddField(
            model_name='product',
            name='total_sales',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
