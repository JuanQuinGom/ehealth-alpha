from django.db import models
from ..personal_data.models import Datos_Personas

# Create your models here.
class Modelos2(models.Model):
    folio = models.ForeignKey(Datos_Personas,null=True,blank=False,on_delete=models.CASCADE)
    #folio = models.CharField(max_length=30)
    peso = models.IntegerField()
    presion_sistolica = models.IntegerField()
    presion_diastolica = models.IntegerField()
    pulso_cardiaco = models.IntegerField()
    frecuencia_respiratoria = models.IntegerField()
    temperatura = models.IntegerField()
    pentavalente = models.BooleanField()
    difterica = models.BooleanField()
    edad = models.IntegerField()
    embarazo_previo = models.BooleanField()
    diagnostico = models.BooleanField()
    #=models.IntegerField()
