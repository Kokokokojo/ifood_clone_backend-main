from django.db import models as db

# Create your models here.

class OrderStatus(db.TextChoices):
    PENDING = 'AG', 'Aguardando'
    IN_PRODUCTION = 'EP', 'Em produção'
    EN_ROUTE = 'ER', 'Em rota de entrega'
    DELIVERED = 'DE', 'Entregue'
    CANCELLED = 'CA', 'Cancelado'

class Order(db.Model):
    description = db.TextField(blank=True, null=True, default="")
    price = db.DecimalField(max_digits=7, decimal_places=2, blank=False, null=False)

    cpf = db.CharField(max_length=11, unique=False, blank=True, null=True)
    cnpj = db.CharField(max_length=14, unique=False, blank=True, null=True)
    email = db.EmailField(max_length=100, unique=False, blank=True, null=True)

    items = db.ManyToManyField('products.Product', blank=True)
    restaurant = db.ForeignKey('restaurants.Restaurant', on_delete=db.CASCADE, null=False, blank=False)
    user = db.ForeignKey("users.CustomUser", on_delete=db.CASCADE, null=False, blank=False)

    created_at = db.DateTimeField(auto_now_add=True)
    status = db.CharField(max_length=20, choices=OrderStatus.choices, default=OrderStatus.PENDING)

    
    def __str__(self):
        return self.description
