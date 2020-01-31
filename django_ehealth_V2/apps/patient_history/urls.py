from django.conf.urls import url

from ..patient_history.views import HistorialPacienteList,HistorialPacienteCreate,HistorialPacienteDelete,HistorialPacienteUpdate

urlpatterns = [
    #url(r'^index$', index_patient),
    url(r'^listar$', HistorialPacienteList.as_view(),name='historial_paciente_listar'),
    url(r'^nuevo$', HistorialPacienteCreate.as_view(),name='historial_paciente_crear'),
    url(r'^editar/(?P<pk>\d+)$', HistorialPacienteUpdate.as_view(),name='historial_paciente_editar'),
    url(r'^eliminar/(?P<pk>\d+)$', HistorialPacienteDelete.as_view(),name='historial_paciente_eliminar'),
]
