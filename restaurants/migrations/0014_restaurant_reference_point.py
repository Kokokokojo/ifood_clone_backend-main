# Generated by Django 4.2.1 on 2024-04-01 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0013_alter_restaurant_complement'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='reference_point',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
    ]
