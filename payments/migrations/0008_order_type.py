# Generated by Django 4.2.1 on 2024-05-16 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0007_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='type',
            field=models.CharField(choices=[('TK', 'Irá retirar o pedido na loja'), ('EP', 'Irá ser entregue')], default='TK', max_length=20),
        ),
    ]
