from django.db import models as db

# Create your models here.

class Product(db.Model):
    name = db.CharField(max_length=75, blank=False, null=False)
    description = db.TextField(blank=False, null=False)
    image = db.ImageField(upload_to="products/logos/%Y/%m/%d", blank=True, null=True)
    price = db.DecimalField(max_digits=7, decimal_places=2, blank=False, null=False)
    total_sales = db.IntegerField(blank=True, null=True, default=0)
    
    restaurant = db.ForeignKey("restaurants.Restaurant", on_delete=db.CASCADE, null=False, blank=False)
    categories = db.ManyToManyField('categories.category', blank=True)
    
    is_active = db.BooleanField(default=True)

    @property
    def restaurant_address(self):
        full_address = ""
        restaurant = self.restaurant  

        full_address = f'{restaurant.street} {restaurant.neighborhood} {restaurant.number}'

        return full_address

    
    def __str__(self):
        return self.name
