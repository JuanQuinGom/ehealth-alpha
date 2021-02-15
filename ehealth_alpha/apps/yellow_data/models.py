# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..personal_data.models import Datos_Personas
# Create your models here.

class Datos_Amarillo(models.Model):
    BLOOD_CHOICES= [
    ('A-','A-'),
    ('A+','A+'),
    ('B-','B-'),
    ('B+','B+'),
    ('AB-','AB-'),
    ('AB+','AB+'),
    ('O-','O-'),
    ('O+','O+'),
    ]
    ESTUDIOS_CHOICES = [
    ('PRIMARIA','Primaria'),
    ('SECUNDARIA','Secundaria'),
    ('BACHILLERATO','Bachillerato'),
    ('UNIVERSIDAD','Universidad'),
    ('POSGRADO','Posgrado'),
    ]
    folio = models.ForeignKey(Datos_Personas,blank=False,null=True,on_delete=models.CASCADE)
    FUM = models.DateField()
    FPP = models.DateField()
    tipo_sangre = models.CharField(max_length=5,choices=BLOOD_CHOICES,default='O+')
    peso = models.DecimalField(max_digits=20,decimal_places=2)
    talla = models.IntegerField()
    etnia = models.CharField(max_length=10)
    fecha_embarazo_anterior = models.DateField(blank=True)
    estudios = models.CharField(max_length=15,choices=ESTUDIOS_CHOICES,default='PRIMARIA')
    cantidad_fetos = models.IntegerField()
