from django.db import models

# Create your models here.

class Libros(models.Model):
    nombre=models.CharField(max_length=60)
    autor=models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    codigo=models.CharField(max_length=100)
    estado=models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

   
    