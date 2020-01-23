from django.db import models
from ..general.models import Vacunas
from ..personal_data.models import Person
# Create your models here.
class Amarilla(models.Model):
    #edad a clave foranea
    #folio a clave foranea
    folio = models.ForeignKey(Person,null=True,blank=True,on_delete=models.CASCADE)
    #edad = models.ForeignKey(person,null=True, blank=True, on_delete=models.CASCADE)
    parejas_sexuales = models.IntegerField()
    gestas_previas = models.IntegerField()
    partos = models.IntegerField()
    abortos = models.IntegerField()
    cesareas = models.IntegerField()
    vaginales = models.IntegerField()
    nacidos_vivos= models.IntegerField()
    viven = models.IntegerField()

class Consultas(models.Model):
    folio = models.ForeignKey(Person,null=True,blank=False,on_delete=models.CASCADE)
    no_consulta= models.IntegerField()
    fecha_consulta=models.DateField()
    edad_gestacional=models.DecimalField(max_digits=20,decimal_places=2)
    peso=models.DecimalField(max_digits=20,decimal_places=2)
    altura_uterina=models.IntegerField()
    FCF=models.IntegerField()
    freq_respiratoria=models.IntegerField()
    glucemia=models.IntegerField()

class Inmunizaciones(models.Model):
    vacunas = models.ManyToManyField(Vacunas)
