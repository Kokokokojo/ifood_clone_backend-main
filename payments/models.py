from django.db import models as db

# Create your models here.

class OrderStatus(db.TextChoices):
    PENDING = 'AG', 'Aguardando'
    IN_PRODUCTION = 'EP', 'Em produção'
    TAKEOUT = 'TK', 'Pedido pronto para retirada'
    EN_ROUTE = 'ER', 'Em rota de entrega'
    DELIVERED = 'DE', 'Entregue'
    CANCELLED = 'CA', 'Cancelado'

class OrderType(db.TextChoices):
    TAKEOUT = 'TK', 'Irá retirar o pedido na loja'
    DELIVERY = 'EE', 'Irá ser entregue'


class Order(db.Model):
    description = db.TextField(blank=True, null=True, default="")
    price = db.DecimalField(max_digits=7, decimal_places=2, blank=False, null=False)

    cpf = db.CharField(max_length=11, unique=False, blank=True, null=True)
    cnpj = db.CharField(max_length=14, unique=False, blank=True, null=True)
    email = db.EmailField(max_length=100, unique=False, blank=True, null=True)

    items = db.ManyToManyField('products.Product', blank=True)
    restaurant = db.ForeignKey('restaurants.Restaurant', on_delete=db.CASCADE, null=False, blank=False)
    user = db.ForeignKey("users.CustomUser", on_delete=db.CASCADE, null=False, blank=False)

    status = db.CharField(max_length=20, choices=OrderStatus.choices, default=OrderStatus.PENDING)
    type = db.CharField(max_length=20, choices=OrderType.choices, default=OrderType.TAKEOUT)

    created_at = db.DateTimeField(auto_now_add=True)
    updated_at = db.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
