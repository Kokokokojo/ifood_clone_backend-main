from django.db import models as db

# Create your models here.


class Category(db.Model):
    name = db.CharField(max_length=75, blank=False, null=False)
    description = db.TextField(blank=False, null=False)
    image = db.ImageField(upload_to="categories/logos/%Y/%m/%d", blank=True, null=True)

    is_active = db.BooleanField(default=True)   


    def __str__(self):
        return self.name