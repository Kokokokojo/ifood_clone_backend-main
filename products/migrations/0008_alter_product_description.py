# Generated by Django 4.2.1 on 2024-04-01 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_delete_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(),
        ),
    ]
