
from django.conf.urls import url

from ..vaccines.views import VacunacionesList, VacunacionesCreate, VacunacionesDelete, VacunacionesUpdate

urlpatterns = [
    #url(r'^index$', index_personal_data, name = 'vacunaciones'),
    url(r'^listar$', VacunacionesList.as_view(),name='vacunaciones_listar'),
    url(r'^nuevo$', VacunacionesCreate.as_view(),name='vacunaciones_crear'),
    url(r'^editar/(?P<pk>\d+)$', VacunacionesUpdate.as_view(),name='vacunaciones_editar'),
    url(r'^eliminar/(?P<pk>\d+)$', VacunacionesDelete.as_view(),name='vacunaciones_eliminar'),

]
