from django import forms

from ..patient_history.models import Historial_Paciente

class HistorialPacienteForm(forms.ModelForm):
    class Meta:
        model = Historial_Paciente
        fields = [
        'folio',
        'enfermedades',
        ]
        labels = {
        'folio':'Folio',
        'enfermedades':'Enfermedades del Paciente'
        }
        widgets ={
        'folio':forms.Select(),
        'enfermedades': forms.CheckboxSelectMultiple()
        }
