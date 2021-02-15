# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..personal_data.models import Datos_Personas
from ..diseases.models import Enfermedades

# Create your models here.
class Historial_Padres(models.Model):
    folio = models.ForeignKey(Datos_Personas,null=True,blank=False,on_delete=models.CASCADE)
    nombre = models.TextField()
    apellido_paterno = models.TextField()
    apellido_materno = models.TextField()
    enfermedades = models.ManyToManyField(Enfermedades)
