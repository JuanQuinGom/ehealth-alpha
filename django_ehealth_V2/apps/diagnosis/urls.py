from django.conf.urls import url

from ..diagnosis.views import  DiagnosticosList,DiagnosticosUpdate,DiagnosticosDelete,DiagnosticosDelete

urlpatterns = [
    #url(r'^index$', index_patient),
    url(r'^listar$', DiagnosticosList.as_view(),name='diagnosticos_listar'),
    url(r'^nuevo$', DiagnosticosCreate.as_view(),name='diagnosticos_crear'),
    url(r'^editar/(?P<pk>\d+)$', DiagnosticosUpdate.as_view(),name='diagnosticos_editar'),
    url(r'^eliminar/(?P<pk>\d+)$', DiagnosticosDelete.as_view(),name='diagnosticos_eliminar'),
]
