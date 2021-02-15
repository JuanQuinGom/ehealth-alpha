from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from ..patient_history.views import HistorialPacienteList,HistorialPacienteCreate,HistorialPacienteDelete,HistorialPacienteUpdate

urlpatterns = [
    #url(r'^index$', index_patient),
    url(r'^modelo$', login_required(HistorialPacienteList.as_view()),name='historial_paciente_listar'),
    
]
