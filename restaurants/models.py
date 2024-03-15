from django.db import models as db

# Create your models here.

class Restaurant(db.Model):
    name = db.CharField(max_length=75, blank=False, null=False)
    description = db.CharField(max_length=100, blank=False, null=False)
    logo = db.ImageField(upload_to="logos/",blank=False, null=False)
    street = db.CharField(max_length=75, blank=False, null=False)
    neighborhood = db.CharField(max_length=75, blank=False, null=False)
    number = db.CharField(max_length=100, blank=False, null=False)
    city = db.CharField(max_length=75, blank=False, null=False)
    state = db.CharField(max_length=75, blank=False, null=False)
    zip_code = db.CharField(max_length=8, blank=False, null=False)
    
    is_active = db.BooleanField(default=True)

    def __str__(self):
        return self.name
