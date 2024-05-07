from django.db import models as db

# Create your models here.

class Order(db.Model):
    description = db.TextField(blank=True, null=True, default="")
    price = db.DecimalField(max_digits=7, decimal_places=2, blank=False, null=False)

    cpf = db.CharField(max_length=11, unique=False, blank=True, null=True)
    cnpj = db.CharField(max_length=14, unique=False, blank=True, null=True)
    email = db.EmailField(max_length=100, unique=False, blank=True, null=True)

    items = db.ManyToManyField('products.Product', blank=True)
    user = db.ForeignKey("users.CustomUser", on_delete=db.CASCADE, null=False, blank=False)
    created_at = db.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.id
