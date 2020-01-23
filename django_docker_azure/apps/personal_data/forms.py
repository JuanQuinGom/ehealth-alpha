from django import forms

from ..personal_data.models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person

        fields=[
        'folio',
        'nombre',
        'apellido_paterno',
        'apellido_materno',
        'edad',
        'fecha_nacimiento',
        'domicilio',
        ]
        labels = {
        'folio': 'Folio',
        'nombre': 'Nombre',
        'apellido_paterno' : 'Apellido Paterno',
        'apellido_materno' : 'Apellido Materno',
        'edad' : 'Edad',
        'fecha_nacimiento' : 'Fecha de Nacimiento',
        'domicilio' : 'Domicilio'
        }

        widgets = {
        'folio' : forms.TextInput(attrs={'class':'form-control'})
        'nombre' : forms.TextInput(attrs={'class':'form-control'})
        'apellido_paterno' : forms.TextInput(attrs={'class':'form-control'})\
        'apellido_materno' : forms.TextInput(attrs={'class':'form-control'})
        'edad' : forms.TextInput(attrs={'class':'form-control'})
        'fecha_nacimiento' : forms.TextInput(attrs={'class':'form-control'})
        'domicilio' : forms.TextInput(attrs={'class':'form-control'})
        }
