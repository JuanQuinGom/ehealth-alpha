from django import forms

from ..diseases.models import Enfermedades

class EnfermedadesForm(forms.ModelForm):
    fields=[
    'codigo',
    'nombre_enfermedad',
    'descripcion',
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
