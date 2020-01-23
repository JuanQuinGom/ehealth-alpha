from django.db import models

# Create your models here.
class Person(models.Model):
    folio = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    edad = models.IntegerField() #a anexar a llave foranea
    fecha_nacimiento = models.DateField()
    domicilio = models.TextField()

    def __str__(self):
        return '{}'.format(self.apellido_paterno, self.apellido_materno, self.nombre)
