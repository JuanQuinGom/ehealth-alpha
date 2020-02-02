from django import forms

from..yellow_data.models import Datos_Amarillo

class DatosAmarilloForm(forms.ModelForm):
    fields=[
    'folio',
    'FUM',
    'FPP',
    'tipo_sangre',
    'peso',
    'talla',
    'etnia',
    'fecha_embarazo_anterior',
    'estudios',
    'cantidad_fetos',
    ]
    labels = {
    'folio':'Folio',
    'FUM':'FUM',
    'FPP':'FPP',
    'tipo_sangre':'Tipo sanguineo',
    'peso':'Peso',
    'talla':'Talla',
    'etnia':'Etnia',
    'fecha_embarazo_anterior':'Fecha último embarazo',
    'estudios':'Estudios',
    'cantidad_fetos':'Cantidad de fetos',
    }

    widgets = {
    'folio' : forms.Select(),
    'FUM' : forms.TextInput(attrs = {'class':'form-control'}),
    'FPP' : forms.TextInput(attrs={'class':'form-control'}),
    'tipo_sangre' : forms.TextInput(attrs={'class':'form-control'}),
    'peso' : forms.TextInput(attrs={'class':'form-control'}),
    'talla' : forms.TextInput(attrs={'class':'form-control'}),
    'etnia' : forms.TextInput(attrs={'class':'form-control'}),
    'fecha_embarazo_anterior' : forms.TextInput(attrs={'class':'form-control'}),
    'estudios' : forms.TextInput(attrs={'class':'form-control'}),
    'cantidad_fetos' : forms.TextInput(attrs={'class':'form-control'}),
    }
