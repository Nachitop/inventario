# Clases abstractas
from django.db import models


status_generic_choices = [
    ('Activo', 'Activo'),
    ('Inactivo', 'Inactivo'),
    ('Reparación','Reparación'),
    ('Prestado','Prestado'),
    ('Entregado','Entregado'),
]


class StatusGeneric(models.Model):

    status = models.CharField(max_length=15,default=status_generic_choices[0], choices=status_generic_choices[0:2])

    class Meta:
        abstract = True


class FechaGeneric(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
