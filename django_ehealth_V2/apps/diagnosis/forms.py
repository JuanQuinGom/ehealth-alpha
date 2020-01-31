from django import forms

from ..personal_data.models import Diagnosticos

class DiagnosticosForm(forms.ModelForm):
    class Meta:
        model = Diagnosticos

        fields=[
        'folio',
        'enfermedades',
        'observaciones'
        ]
        labels = {
        'folio': 'Folio',
        'enfermedades': 'Nombre',
        'observaciones' : 'Observaciones'
        }

        widgets = {
        'folio' : forms.TextInput(attrs={'class':'form-control'}),
        'enfermedades' : forms.TextInput(attrs = {'class':'form-control'}),
        'observaciones' : forms.TextInput(attrs={'class':'form-control'}),
        }
