from django.db import models as db

# Create your models here.

class Product(db.Model):
    name = db.CharField(max_length=75, blank=False, null=False)
    description = db.CharField(max_length=100, blank=False, null=False)
    image = db.ImageField(upload_to="products/logos/%Y/%m/%d", blank=True, null=True)
    price = db.DecimalField(max_digits=7, decimal_places=2, blank=False, null=False)
    qtd = db.IntegerField(blank=False, null=False)
    
    restaurant = db.ForeignKey("restaurants.Restaurant", on_delete=db.CASCADE, null=False, blank=False)
    
    is_active = db.BooleanField(default=True)

    
    def __str__(self):
        return self.name


class Category(db.Model):
    name = db.CharField(max_length=75, blank=False, null=False)
    description = db.CharField(max_length=100, blank=False, null=False)
    product = db.ForeignKey(Product, on_delete=db.SET_NULL, null=True, blank=False)

    is_active = db.BooleanField(default=True)   



    def __str__(self):
        return self.name