# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..personal_data.models import Datos_Personas
from ..vaccines.models import Vacunaciones
# Create your models here.
# -*- coding: utf-8 -*-

class Inmunizaciones(models.Model):
    folio = models.ForeignKey(Datos_Personas,null=True,blank=False,on_delete=models.CASCADE)
    vacunas_inyectadas = models.ManyToManyField(Vacunaciones)
