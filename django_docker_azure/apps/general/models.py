from django.db import models

# Create your models here.
class Vacunas(models.Model):
    folio_vacuna = models.CharField(max_length=30)
    nombre_vacuna=models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.folio, self.nombre)
