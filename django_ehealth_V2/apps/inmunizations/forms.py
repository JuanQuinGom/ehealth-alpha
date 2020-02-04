from django import forms

from ..inmunizations.models import Inmunizaciones

class InmunizacionesForm(forms.ModelForm):
    class Meta:
        model = Inmunizaciones

        fields=[
        'folio',
        'vacunas_inyectadas',
        ]
        labels = {
        'folio':'Folio',
        'vacunas_inyectadas':'Esquema de Vacunacion',
        }

        widgets = {
        'folio' : forms.Select(),
        'vacunas_inyectadas':forms.CheckboxSelectMultiple(),
        }
