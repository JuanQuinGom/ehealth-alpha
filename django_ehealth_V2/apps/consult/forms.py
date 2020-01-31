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
    'folio': 'Folio',
    'no_consulta': 'No. de Consulta',
    'fecha_consulta' : 'Fecha de Consulta',
    'edad_gestacional' : 'Edad Gestacional',
    'peso' : 'Peso',
    'altura_uterina' : 'Altura Uterina',
    'FCF' : 'FCF',
    'freq_respiratoria' : 'Frecuencia Respiratoria',
    'glucemia' : 'Glucemia',
    }

    widgets = {
    'folio' : forms.TextInput(attrs={'class':'form-control'}),
    'no_consulta' : forms.TextInput(attrs = {'class':'form-control'}),
    'fecha_consulta' : forms.TextInput(attrs={'class':'form-control'}),
    'edad_gestacional' : forms.TextInput(attrs={'class':'form-control'}),
    'peso' : forms.TextInput(attrs={'class':'form-control'}),
    'altura_uterina' : forms.TextInput(attrs={'class':'form-control'}),
    'FCF' : forms.TextInput(attrs={'class':'form-control'}),
    'glucemia' : forms.TextInput(attrs={'class':'form-control'}),

    }
