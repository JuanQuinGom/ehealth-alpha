
from django.conf.urls import url

from ..inmunizations.views import InmunizacionesList, InmunizacionesCreate, InmunizacionesDelete, InmunizacionesUpdate

urlpatterns = [
    #url(r'^index$', index_personal_data, name = 'Inmunizaciones'),
    url(r'^listar$', InmunizacionesList.as_view(),name='inmunizaciones_listar'),
    url(r'^nuevo$', InmunizacionesCreate.as_view(),name='inmunizaciones_crear'),
    url(r'^editar/(?P<pk>\d+)$', InmunizacionesUpdate.as_view(),name='inmunizaciones_editar'),
    url(r'^eliminar/(?P<pk>\d+)$', InmunizacionesDelete.as_view(),name='inmunizaciones_eliminar'),

]
