from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    foodType = models.CharField(max_length=255)
    spots = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Hotel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    starts = models.IntegerField()
    
    def __str__(self):
        return self.name

class AdminUserManager(BaseUserManager):
    def create_user(self, correo, contrasena=None, **extra_fields):
        if not correo:
            raise ValueError("El correo es obligatorio")
        correo = self.normalize_email(correo)
        user = self.model(correo=correo, **extra_fields)
        user.set_password(contrasena)  
        user.save(using=self._db)
        return user

    def create_superuser(self, correo, contrasena, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(correo, contrasena, **extra_fields)

class AdminUser(AbstractBaseUser, PermissionsMixin):
    correo = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    is_employee = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)

    objects = AdminUserManager()  

    USERNAME_FIELD = "correo"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.name
    
class PlanViaje(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    days = models.IntegerField()
    budget = models.IntegerField()
    user = models.ForeignKey(AdminUser, on_delete=models.CASCADE, related_name="planes_viaje")
    restaurantes = models.ManyToManyField('Restaurant', related_name="planes_viaje", blank=True)
    hoteles = models.ManyToManyField('Hotel', related_name="planes_viaje", blank=True)
    
    def __str__(self):
        return self.name
    
    