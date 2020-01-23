from django import forms

from ..general.models import Vacunas

class GeneralForm(forms.ModelForm):
    class Meta:
        model = Vacunas

        fields = [
        'nombre_vacuna',
        ]
        labels = { #etiquetas al ingresar
        'folio_vacuna' : 'Folio o Codigo de Vacuna'
        'nombre_vacuna' : 'Nombre de Vacuna',
        }
        widgets = { #etiquetas a pintar tipo html
        'folio_vacuna' : forms.TextInput(attrs={'class': form-control}),
        'nombre_vacuna': forms.TextInput(attrs={'class':'form-control'}),
        #para foriegnKey usan forms.Select
        #para manyToMany forms.CheckboxSelectMultiple(),
        }
