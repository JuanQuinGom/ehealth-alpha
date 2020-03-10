from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from ..diseases.views import EnfermedadesList, EnfermedadesCreate, EnfermedadesDelete, EnfermedadesUpdate

urlpatterns = [
    #url(r'^index$', index_personal_data, name = 'enfermedades'),
    url(r'^listar$', login_required(EnfermedadesList.as_view()),name='enfermedades_listar'),
    url(r'^nuevo$', login_required(EnfermedadesCreate.as_view()),name='enfermedades_crear'),
    url(r'^editar/(?P<pk>\d+)$', login_required(EnfermedadesUpdate.as_view()),name='enfermedades_editar'),
    url(r'^eliminar/(?P<pk>\d+)$', login_required(EnfermedadesDelete.as_view()),name='enfermedades_eliminar'),

]
