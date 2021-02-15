# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Enfermedades(models.Model):
    codigo = models.CharField(max_length=10)
    nombre_enfermedad = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return '{}'.format(self.nombre_enfermedad)
