# Generated by Django 4.2.1 on 2024-05-16 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0009_alter_order_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
