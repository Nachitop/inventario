from django.db import models
from inventario.abstract_classes import FechaGeneric, StatusGeneric
# Create your models here.


class Edificio(FechaGeneric, StatusGeneric):
    nombre = models.CharField(max_length=15)

    def __str__(self):
        return '{}'.format(self.nombre)


class Ubicacion(FechaGeneric, StatusGeneric):
    nombre = models.CharField(max_length=25)
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre)
