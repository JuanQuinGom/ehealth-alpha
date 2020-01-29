# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..personal_data.models import Datos_Personas
from ..diseases.models import Enfermedades

# Create your models here.
class Historial_Paciente(models.Model):
    folio = models.ForeignKey(Datos_Personas,null=True,blank=False,on_delete=models.CASCADE)
    enfermedades = models.ManyToManyField(Enfermedades)
