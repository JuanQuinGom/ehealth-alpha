# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..personal_data.models import Datos_Personas
# Create your models here.
    folio = models.ForeignKey(Datos_Personas,null=True,blank=False,on_delete=models.CASCADE)
    no_registro= models.IntegerField()
    id_device=models.IntegerField()
    fecha_registro=models.DateField()
    presion_diastolica=models.IntegerField()
    presion_sistolica=models.IntegerField()
    pulso_cardiaco=models.IntegerField()
    temperatura=models.IntegerField()
    #=models.IntegerField()
