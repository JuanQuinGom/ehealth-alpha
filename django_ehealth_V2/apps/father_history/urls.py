
from django.conf.urls import url

from ..father_history.views import Historial_PadresList, Historial_PadresCreate, Historial_PadresDelete, Historial_PadresUpdate

urlpatterns = [
    #url(r'^index$', index_personal_data, name = 'historial_padres'),
    url(r'^listar$', Historial_PadresList.as_view(),name='historial_padres_listar'),
    url(r'^nuevo$', Historial_PadresCreate.as_view(),name='historial_padres_crear'),
    url(r'^editar/(?P<pk>\d+)$', Historial_PadresUpdate.as_view(),name='historial_padres_editar'),
    url(r'^eliminar/(?P<pk>\d+)$', Historial_PadresDelete.as_view(),name='historial_padres_eliminar'),

]
