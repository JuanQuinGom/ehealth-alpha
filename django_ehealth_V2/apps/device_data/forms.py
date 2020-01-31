from django import forms

from ..diseases.models import Enfermedades

class EnfermedadesForm(forms.ModelForm):
    fields=[
    'folio',
    'no_registro',
    'id_device',
    'fecha_registro',
    'presion_diastolica',
    'presion_sistolica',
    'pulso_cardiaco',
    'temperatura',
    ]
    labels = {
    'folio': 'Folio',
    'no_registro': 'No. Registro',
    'id_device' : 'ID dispositivo',
    'fecha_registro': 'Fecha del registro',
    'presion_sistolica': 'Presion Sistolica',
    'presion_diastolica' : 'Presion Diastolica',
    'pulso_cardiaco': 'Ritmo Cardiaco (ppm)',
    'temperatura': 'Temperatura',
    }

    widgets = {
    'codigo' : forms.TextInput(attrs={'class':'form-control'}),
    'nombre_enfermedad' : forms.TextInput(attrs = {'class':'form-control'}),
    'descripcion' : forms.TextInput(attrs={'class':'form-control'}),
    }
