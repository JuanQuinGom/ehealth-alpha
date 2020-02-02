from django.conf.urls import url

from ..diseases.views import EnfermedadesList, EnfermedadesCreate, EnfermedadesDelete, EnfermedadesUpdate

urlpatterns = [
    #url(r'^index$', index_personal_data, name = 'enfermedades'),
    url(r'^listar$', EnfermedadesList.as_view(),name='enfermedades_listar'),
    url(r'^nuevo$', EnfermedadesCreate.as_view(),name='enfermedades_crear'),
    url(r'^editar/(?P<pk>\d+)$', EnfermedadesUpdate.as_view(),name='enfermedades_editar'),
    url(r'^eliminar/(?P<pk>\d+)$', EnfermedadesDelete.as_view(),name='enfermedades_eliminar'),

]
