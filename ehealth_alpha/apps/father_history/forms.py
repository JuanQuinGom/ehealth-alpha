from django import forms

from..father_history.models import Historial_Padres

class HistorialPadresForm(forms.ModelForm):
    class Meta:
        model = Historial_Padres
        fields=[
        'folio',
        'nombre',
        'apellido_materno',
        'apellido_paterno',
        'enfermedades',
        ]
        labels = {
        'folio': 'Folio',
        'nombre': 'Folio',
        'apellido_paterno': 'Apellido Paterno',
        'apellido_materno': 'Apellido Materno',
        'enfermedades': 'Enfermedades Padecidas',
        }

        widgets = {
        'folio' : forms.Select(),
        'nombre' : forms.TextInput(attrs = {'class':'form-control'}),
        'apellido_paterno' : forms.TextInput(attrs={'class':'form-control'}),
        'apellido_materno' : forms.TextInput(attrs={'class':'form-control'}),
        'enfermedades' : forms.CheckboxSelectMultiple(),
        }
