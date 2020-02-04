from django import forms

from..obstetrical_data.models import Datos_Obstetricos

class DatosObstetricosForm(forms.ModelForm):
    class Meta:
        model = Datos_Obstetricos
        fields=[
        'folio',
        'parejas_sexuales',
        'gestas_previas',
        'partos',
        'abortos',
        'cesareas',
        'vaginales',
        'nacidos_vivos',
        'viven',
        ]
        labels = {
        'folio': 'Folio',
        'parejas_sexuales': 'Parejas Sexuales',
        'gestas_previas': 'Gestas Previas',
        'partos':'Partos',
        'abortos':'Abortos',
        'cesareas':'Cesareas',
        'vaginales':'Vaginales',
        'nacidos_vivos':'Nacidos Vivos',
        'viven':'Viven',
        }

        widgets = {
        'folio' : forms.Select(),
        'parejas_sexuales' : forms.TextInput(attrs = {'class':'form-control'}),
        'gestas_previas' : forms.TextInput(attrs={'class':'form-control'}),
        'partos' : forms.TextInput(attrs={'class':'form-control'}),
        'abortos' : forms.TextInput(attrs={'class':'form-control'}),
        'cesareas' : forms.TextInput(attrs={'class':'form-control'}),
        'vaginales' : forms.TextInput(attrs={'class':'form-control'}),
        'nacidos_vivos' : forms.TextInput(attrs={'class':'form-control'}),
        'viven' : forms.TextInput(attrs={'class':'form-control'}),
        }
