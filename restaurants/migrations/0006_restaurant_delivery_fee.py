# Generated by Django 4.2.1 on 2024-03-20 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_restaurant_cnpj'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='delivery_fee',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=7),
            preserve_default=False,
        ),
    ]
