from django import forms

from ..preg_historial.models import Amarilla,Consultas,Inmunizaciones

class AmarillaForm(forms.ModelForm):
    class Meta:
        fields = [
        'folio',
        'parejas_sexuales',
        'gestas_previas',
        'partos',
        'abortos',
        'cesareas',
        'vaginales',
        'nacidos_vivos',
        'viven'
        ]
        labels = {
        'folio' : 'No. de Folio',
        'parejas_sexuales' : 'Numero de Parejas Sexuales',
        'gestas_previas' : 'Gestas Previas',
        'partos' : 'Partos',
        'abortos' : 'Abortos',
        'cesareas' : 'Cesáreas',
        'vaginales' : 'Vaginales',
        'nacidos_vivos' : 'Nacidos Vivos',
        'viven' : 'Viven',
        }
        widgets = {
        'folio' : forms.Select()
        'parejas_sexuales' : forms.TextInput(attrs={'class':'form-control'}),
        'gestas_previas' : forms.TextInput(attrs={'class':'form-control'}),
        'partos' : forms.TextInput(attrs={'class':'form-control'}),
        'abortos' : forms.TextInput(attrs={'class':'form-control'}),
        'cesareas' : forms.TextInput(attrs={'class':'form-control'}),
        'vaginales' : forms.TextInput(attrs={'class':'form-control'}),
        'nacidos_vivos' : forms.TextInput(attrs={'class':'form-control'}),
        'viven' : forms.TextInput(attrs={'class':'form-control'}),
        }

class ConsultaForm (forms.ModelForm):
    class Meta:
        model = Consultas

        fields = [
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
        'folio': 'No. de Folio',
        'no_consulta' : 'No. de Consulta',
        'fecha_consulta' : 'Fecha de Consulta',
        'edad_gestacional' : 'Edad Gestacional',
        'peso' : 'Peso',
        'altura_uterina' : 'Altura Uterina',
        'FCF' : 'Frecuencia Cardiaca del Feto',
        'freq_respiratoria' : 'Frecuencia Respiratoria',
        'glucemia' : 'Glucemia',
        }
        widgets = {
        'folio': forms.Select()
        'no_consulta' : forms.TextInput(attrs={'class':'form-control'}),
        'fecha_consulta' : forms.TextInput(attrs={'class':'form-control'}),
        'edad_gestacional' : forms.TextInput(attrs={'class':'form-control'}),
        'peso' : forms.TextInput(attrs={'class':'form-control'}),
        'altura_uterina' : forms.TextInput(attrs={'class':'form-control'}),
        'FCF' : forms.TextInput(attrs={'class':'form-control'}),
        'freq_respiratoria' : forms.TextInput(attrs={'class':'form-control'}),
        'glucemia' : forms.TextInput(attrs={'class':'form-control'}),
        }

class InmunizacionesForm(forms.ModelForm):
    class Meta:
        model = Inmunizaciones

        fields = [
        'vacunas',
        ]
        labels = {

        }
