from django.db import models
from inventario.abstract_classes import FechaGeneric, status_generic_choices
from equipos.models import Equipo
from facultades.models import Ubicacion
from django.core.exceptions import ValidationError

# Create your models here.


class Movimiento(FechaGeneric):
    numero_cuenta = models.CharField(max_length=9)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=15, default=status_generic_choices[3], choices=status_generic_choices[3:5])

    def actualizarEquipo(self):

        equipo = Equipo.objects.filter(pk=self.equipo.pk).last()
        if equipo.status == status_generic_choices[0][0]:
            print(status_generic_choices[3][0])
            print("alv")
            equipo.status = status_generic_choices[3][0]
            print(equipo.status)
            equipo.save()
        else:
            raise ValidationError("No se pueden entregar equipos que no estén disponibles")

    def clean(self):
        if self.pk is None:
            ultimo_movimiento = Movimiento.objects.filter(numero_cuenta=self.numero_cuenta).last()
            if ultimo_movimiento:
                if ultimo_movimiento.status == status_generic_choices[3][0]:
                    raise ValidationError("No se puede efectuar el prestamo, esta matricula tiene pendientes de entrega")
                else:
                    self.actualizarEquipo()
            else:
                self.actualizarEquipo()    
        else:
            if self.status == status_generic_choices[3][0]:
                raise ValidationError("No puede cambair el status de Entregado a Prestado")
            elif self.status == status_generic_choices[4][0] and self.equipo.status == status_generic_choices[3][0]:
                Equipo.objects.filter(pk=self.equipo.pk).update(status = status_generic_choices[0][0])            


    def __str__(self):
        return '{}-{},{}-{}-{}'.format(self.numero_cuenta, self.equipo.tipo_equipo.nombre, self.equipo.marca.nombre, self.ubicacion.nombre, self.status)
