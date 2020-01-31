from django import forms

from ..consult.models import Consultas

class ConsultasForm(forms.ModelForm):
    fields=[
    'folio',
    'no_consulta',
    'fecha_consulta',
    'edad_gestacional',
    'peso',
    'altura_uterina',
    'FCF',
    'freq_respiratoria',
    'glucemia',
    ]
    labels = {
    'codigo': 'Clave de Enfermedad',
    'nombre_enfermedad': 'Nombre de Enfermedad o Padecimiento',
    'descripcion' : 'descripcion',
    }

    widgets = {
    'codigo' : forms.TextInput(attrs={'class':'form-control'}),
    'nombre_enfermedad' : forms.TextInput(attrs = {'class':'form-control'}),
    'descripcion' : forms.TextInput(attrs={'class':'form-control'}),
    }
