
from django.conf.urls import url

from ..obstetrical_data.views import DatosObstetricosList, DatosObstetricosCreate, DatosObstetricosDelete, DatosObstetricosUpdate

urlpatterns = [
    #url(r'^index$', index_personal_data, name = 'datos_obstetricos'),
    url(r'^listar$', DatosObstetricosList.as_view(),name='datos_obstetricos_listar'),
    url(r'^nuevo$', DatosObstetricosCreate.as_view(),name='datos_obstetricos_crear'),
    url(r'^editar/(?P<pk>\d+)$', DatosObstetricosUpdate.as_view(),name='datos_obstetricos_editar'),
    url(r'^eliminar/(?P<pk>\d+)$', DatosObstetricosDelete.as_view(),name='datos_obstetricos_eliminar'),

]
