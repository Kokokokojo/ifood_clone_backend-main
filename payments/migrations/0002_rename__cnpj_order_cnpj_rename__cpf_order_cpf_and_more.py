# Generated by Django 4.2.1 on 2024-05-07 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='_cnpj',
            new_name='cnpj',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='_cpf',
            new_name='cpf',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='_email',
            new_name='email',
        ),
    ]