from django.db import models

# Create your models here.
class Vivero(models.Model):
    nombrempresa= models.CharField(max_length=30)
    propietario=models.CharField(max_length=30, unique=True)
    cantorq=models.CharField(max_length=5)
    contacto=models.CharField(max_length=9)
    ubicacion=models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nombrempresa}' 