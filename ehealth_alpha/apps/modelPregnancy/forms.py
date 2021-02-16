from django import forms

from ..modelPregnancy.models import Modelos2

class ModelosPregnancyForm(forms.ModelForm):
    class Meta:
        model = Modelos2

        fields=[
        'folio',
        'peso',
        'presion_sistolica',
        'presion_diastolica',
        'pulso_cardiaco',
        'frecuencia_respiratoria',
        'temperatura',
        'pentavalente',
        'difterica',
        'edad',
        'embarazo_previo',
        'diagnostico',

        ]
        labels = {
        'folio': 'Folio',
        'peso':'Peso',
        'presion_sistolica':'Presión sistólica',
        'presion_diastolica':'Presión diastólica',
        'pulso_cardiaco':'Pulso cardíaco',
        'frecuencia_respiratoria':'Frecuencia respiratoria',
        'temperatura':'Temperatura',
        'pentavalente':'Vacuna pentavalente',
        'difterica':'Vacuna difterica',
        'edad':'Edad',
        'embarazo_previo':'Embarazo previo',
        'diagnostico':'Diagnóstico',
        }

        widgets = {
        'folio': forms.Select(),
        'peso': forms.TextInput(attrs={'class':'form-control'}),
        'presion_sistolica': forms.TextInput(attrs={'class':'form-control'}),
        'presion_diastolica': forms.TextInput(attrs={'class':'form-control'}),
        'pulso_cardiaco': forms.TextInput(attrs={'class':'form-control'}),
        'frecuencia_respiratoria': forms.TextInput(attrs={'class':'form-control'}),
        'temperatura': forms.TextInput(attrs={'class':'form-control'}),
        'pentavalente': forms.TextInput(attrs={'class':'form-control'}),
        'difterica': forms.TextInput(attrs={'class':'form-control'}),
        'edad': forms.TextInput(attrs={'class':'form-control'}),
        'embarazo_previo': forms.TextInput(attrs={'class':'form-control'}),
        'diagnostico': forms.TextInput(attrs={'class':'form-control'}),
        }
