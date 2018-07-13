from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile-pics',blank=True)

    def __str__(self):
        return self.user.username

class Puesto(models.Model):

    nombre = models.CharField(max_length=256)
    descripcion = models.CharField(max_length=256)

    def __str__(self):
        return self.nombre

class Empleado(models.Model):

    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE)
    email = models.EmailField(max_length=256)

    def __str__(self):
        return self.nombre
