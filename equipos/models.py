from django.db import models
from inventario.abstract_classes import FechaGeneric, status_generic_choices
# Create your models here.


class Marca(FechaGeneric):
    nombre = models.CharField(max_length=25)

    def __str__(self):
        return '{}'.format(self.nombre)


class TipoEquipo(FechaGeneric):
    nombre = models.CharField(max_length=25)

    def __str__(self):
        return '{}'.format(self.nombre)

class Equipo(FechaGeneric):
    codigo = models.CharField(max_length=25, unique=True)
    descripcion = models.TextField(max_length=100, default="...")
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    tipo_equipo = models.ForeignKey(TipoEquipo, on_delete= models.CASCADE)
    status = models.CharField(max_length=15,default = status_generic_choices[0] ,choices= status_generic_choices[0:4])

    def __str__(self):
        return '{}-{}-{}'.format(self.codigo,self.marca.nombre,self.tipo_equipo.nombre)