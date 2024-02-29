from django.db import models as db
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, username, first_name, password, **other):
        
        if not email: 
            raise ValueError("You must provide an email address.")
        
        email = self.normalize_email(email)
        user = self.model(email = email, username = username, first_name = first_name, **other)
        
        user.set_password(password)
        user.save()

        return user


    def create_superuser(self, email, username, first_name, password, **other):
        other.setdefault('is_staff', True)
        other.setdefault('is_superuser', True)
        other.setdefault('is_active', True)

        if other.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        
        if other.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')
        
        return self.create_user(email, username, first_name, password, **other)   







class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = db.CharField(max_length=50, blank=True, null=False)
    last_name = db.CharField(max_length=50, blank=True, null=True)


    username = db.CharField(max_length=25, blank=True, null=True, unique=True)
    cpf = db.CharField(max_length=11, unique=True, blank=True, null=True)
    cnpj = db.CharField(max_length=14, unique=True, blank=True, null=True)

    phone = db.CharField(max_length=20, blank=True, null=True)
    email = db.EmailField(max_length=45, unique=True, blank=True, null=True)

    otp = db.CharField(max_length=6, null=True, blank=True) 
    google_id = db.CharField(max_length=21,null=True, blank=True)


    created_at = db.DateTimeField(auto_now_add=True)
    updated_at = db.DateTimeField(auto_now=True)
    
    is_active = db.BooleanField(default=True)
    is_staff = db.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']




    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.first_name
    



class Address(db.Model):
    name = db.CharField(max_length=75, blank=False, null=False)
    street = db.CharField(max_length=75, blank=False, null=False)
    neighborhood = db.CharField(max_length=75, blank=False, null=False)
    number = db.CharField(max_length=75, blank=False, null=False)
    complement = db.CharField(max_length=75, blank=False, null=False)
    city = db.CharField(max_length=75, blank=False, null=False)
    state = db.CharField(max_length=75, blank=False, null=False)

    user = db.ForeignKey(CustomUser, on_delete=db.SET_NULL, null=True, blank=False)

    is_active = db.BooleanField(default=True)


    def __str__(self):
        return self.name
