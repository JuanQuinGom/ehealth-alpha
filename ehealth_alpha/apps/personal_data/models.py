# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Datos_Personas(models.Model):
    folio = models.CharField(max_length = 20)
    nombre = models.CharField(max_length = 50)
    apellido_paterno = models.CharField(max_length = 50)
    apellido_materno = models.CharField(max_length = 50)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    domicilio = models.TextField()

    def __str__(self):
        return '{}'.format(self.folio)
