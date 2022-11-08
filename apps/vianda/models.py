from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class ItemVianda(models.Model):
    descripcion = models.CharField(max_length=20)
    esta_activo = models.BooleanField()

class InfoSolicitudVianda(models.Model):
    FRECUENCIA_OPCIONES = [
        (1,'semanal'),
        (2,'quincenal'),
    ]

    TIPO_MENU = [
        (1,'Normal'),
        (2,'Vegetariano'),
        (3,'Diabetico')
    ]

    ESTADO_VIANDA = [
        (1,'Pendiente'),
        (2,'Confirmado'),
        (3,'Cancelado')
    ]
    tipoMenu = models.IntegerField(null=False, blank=False, choices=TIPO_MENU)
    frecuencia = models.IntegerField(null=False, blank=False, choices=FRECUENCIA_OPCIONES)
    fechaInicioVianda = models.DateField()
    # fechaActual = models.DateField(default=datetime.now())
    cantidadViandas = models.IntegerField(null=False, blank=False)
    estadoVianda = models.IntegerField(null=False, blank=False,choices=ESTADO_VIANDA, default=1)
    itemsincluir = models.ManyToManyField(ItemVianda)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False, default=User.username)
