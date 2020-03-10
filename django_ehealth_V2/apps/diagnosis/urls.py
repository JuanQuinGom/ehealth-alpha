from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from ..diagnosis.views import  DiagnosticosList,DiagnosticosUpdate,DiagnosticosCreate,DiagnosticosDelete

urlpatterns = [
    #url(r'^index$', index_patient),
    url(r'^listar$', login_required(DiagnosticosList.as_view()),name='diagnosticos_listar'),
    url(r'^nuevo$', login_required(DiagnosticosCreate.as_view()),name='diagnosticos_crear'),
    url(r'^editar/(?P<pk>\d+)$', login_required(DiagnosticosUpdate.as_view()),name='diagnosticos_editar'),
    url(r'^eliminar/(?P<pk>\d+)$', login_required(DiagnosticosDelete.as_view()),name='diagnosticos_eliminar'),
]
