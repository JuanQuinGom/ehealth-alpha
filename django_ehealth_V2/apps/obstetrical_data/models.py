# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..personal_data.models import Datos_Personas

# Create your models here.
class Datos_Obstetricos(models.Model):
    folio = models.ForeignKey(Datos_Personas,blank=False,null=True,on_delete=models.CASCADE)
    parejas_sexuales = models.IntegerField()
    gestas_previas = models.IntegerField()
    partos = models.IntegerField()
    abortos = models.IntegerField()
    cesareas = models.IntegerField()
    vaginales = models.IntegerField()
    nacidos_vivos = models.IntegerField()
    viven = models.IntegerField()
