from django.db import models

# Create your models here.

class Orquidea(models.Model):
    tipo_crecimiento= models.CharField(max_length=30)
    nombre_comun=models.CharField(max_length=30, unique=True)
    floracion=models.CharField(max_length=30)
    duracion_flor=models.CharField(max_length=30)
    tamaño_flor=models.CharField(max_length=30)
    ubicacion=models.CharField(max_length=60)

    def __str__(self):
        return f'{self.nombre_comun}' 
        