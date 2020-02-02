from django import forms

from..vaccines.models import Vacunaciones

class VacunacionesForm(forms.ModelForm):
    fields=[
    'codigo',
    'nombre',
    'descripcion',
    ]
    labels = {
    'codigo': 'Código de Vacuna',
    'nombre': 'Folio',
    'descripcion': 'Descripción',
    }

    widgets = {
    'codigo' : forms.TextInput(attrs = {'class':'form-control'}),
    'nombre' : forms.TextInput(attrs={'class':'form-control'}),
    'descripcion' : forms.TextInput(attrs={'class':'form-control'}),
    }
