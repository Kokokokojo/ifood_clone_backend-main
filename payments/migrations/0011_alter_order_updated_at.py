# Generated by Django 4.2.1 on 2024-05-21 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0010_order_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]