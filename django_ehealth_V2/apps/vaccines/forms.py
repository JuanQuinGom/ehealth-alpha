from django import forms

from ..vaccines.models import Vacunaciones

class VacunacionesForm(forms.ModelForm):
    fields=[
    'codigo',
    'nombre',
    'descripcion',
    ]
    labels = {
    'codigo': 'Codigo de Vacuna',
    'nombre': 'Folio',
    'descripcion': 'Descripcion',
    }

    widgets = {
    'codigo' : forms.TextInput(attrs = {'class':'form-control'}),
    'nombre' : forms.TextInput(attrs={'class':'form-control'}),
    'descripcion' : forms.TextInput(attrs={'class':'form-control'}),
    }
