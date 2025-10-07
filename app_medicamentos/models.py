from django.db import models

# Create your models here.

class medicamentos(models.Model):
    nombre= models.CharField()
    funcion= models.CharField()
    precio= models.FloatField()

    def __str__(self):
        return f"{self.nombre} {self.precio}"
