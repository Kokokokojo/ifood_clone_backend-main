# Generated by Django 4.2.1 on 2024-03-07 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_customuser_email_confirmed_in_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email_confirmed_in',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_confirmed_in',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
