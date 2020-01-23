from django.contrib import admin

# Register your models here.
from ..preg_historial.models import Amarilla,Consultas,Inmunizaciones

admin.site.register(Amarilla)
admin.site.register(Consultas)
admin.site.register(Inmunizaciones)
