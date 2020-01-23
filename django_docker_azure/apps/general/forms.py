from django import forms

from ..general.models import Vacunas

class GeneralForm(forms.ModelForm):
    class Meta:
        model = Vacunas

        fields = [
        'nombre',
        ]
        labels = { #etiquetas al ingresar
        'nombre' : 'Nombre de Vacuna',
        }
        widgets = { #etiquetas a pintar tipo html
        'nombre': forms.TextInput(attrs={'class':'form-control'}),
        #para foriegnKey usan forms.Select
        #para manyToMany forms.CheckboxSelectMultiple(),
        }
