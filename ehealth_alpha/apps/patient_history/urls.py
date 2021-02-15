from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from ..patient_history.views import HistorialPacienteList,HistorialPacienteCreate,HistorialPacienteDelete,HistorialPacienteUpdate

urlpatterns = [
    #url(r'^index$', index_patient),
    url(r'^listar$', login_required(HistorialPacienteList.as_view()),name='historial_paciente_listar'),
    url(r'^nuevo$', login_required(HistorialPacienteCreate.as_view()),name='historial_paciente_crear'),
    url(r'^editar/(?P<pk>\d+)$', login_required(HistorialPacienteUpdate.as_view()),name='historial_paciente_editar'),
    url(r'^eliminar/(?P<pk>\d+)$', login_required(HistorialPacienteDelete.as_view()),name='historial_paciente_eliminar'),
]
