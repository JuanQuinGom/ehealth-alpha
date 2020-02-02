from django import forms

from ..diseases.models import Dispositivos

class DispositivosForm(forms.ModelForm):
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
    'folio': forms.TextInput(attrs={'class':'form-control'}),
    'no_registro': forms.TextInput(attrs={'class':'form-control'}),
    'id_device' : forms.TextInput(attrs={'class':'form-control'}),
    'fecha_registro': forms.TextInput(attrs={'class':'form-control'}),
    'presion_sistolica': forms.TextInput(attrs={'class':'form-control'}),
    'presion_diastolica' : forms.TextInput(attrs={'class':'form-control'}),
    'pulso_cardiaco': forms.TextInput(attrs={'class':'form-control'}),
    'temperatura': forms.TextInput(attrs={'class':'form-control'}),
    }
