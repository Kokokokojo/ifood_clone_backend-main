from django.db import models as db

# Create your models here.


class Address(db.Model):
    name = db.CharField(max_length=75, blank=False, null=False)
    street = db.CharField(max_length=75, blank=False, null=False)
    neighborhood = db.CharField(max_length=75, blank=False, null=False)
    number = db.CharField(max_length=75, blank=False, null=False)
    complement = db.CharField(max_length=75, blank=False, null=False)
    city = db.CharField(max_length=75, blank=False, null=False)
    state = db.CharField(max_length=75, blank=False, null=False)
    zip_code = db.CharField(max_length=8, blank=False, null=False)

    user = db.ForeignKey('users.CustomUser', on_delete=db.SET_NULL, null=True, blank=False)

    is_active = db.BooleanField(default=True)


    def __str__(self):
        return self.name