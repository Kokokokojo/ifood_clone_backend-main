# Generated by Django 4.2.1 on 2024-05-16 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0006_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('AG', 'Aguardando'), ('EP', 'Em produção'), ('TK', 'Pedido pronto para retirada'), ('ER', 'Em rota de entrega'), ('DE', 'Entregue'), ('CA', 'Cancelado')], default='AG', max_length=20),
        ),
    ]
