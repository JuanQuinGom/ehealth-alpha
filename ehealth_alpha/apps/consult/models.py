# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..personal_data.models import Datos_Personas

# Create your models here.
class Consultas(models.Model):
    folio = models.ForeignKey(Datos_Personas,null=True,blank=False,on_delete=models.CASCADE)
    no_consulta= models.IntegerField()
    fecha_consulta=models.DateField()
    edad_gestacional=models.DecimalField(max_digits=20,decimal_places=2)
    peso=models.DecimalField(max_digits=20,decimal_places=2)
    altura_uterina=models.IntegerField()
    FCF=models.IntegerField()
    freq_respiratoria=models.IntegerField()
    glucemia=models.IntegerField()
