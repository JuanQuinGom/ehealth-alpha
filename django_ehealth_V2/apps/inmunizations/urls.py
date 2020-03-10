
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from ..inmunizations.views import InmunizacionesList, InmunizacionesCreate, InmunizacionesDelete, InmunizacionesUpdate

urlpatterns = [
    #url(r'^index$', index_personal_data, name = 'Inmunizaciones'),
    url(r'^listar$', login_required(InmunizacionesList.as_view()),name='inmunizaciones_listar'),
    url(r'^nuevo$', login_required(InmunizacionesCreate.as_view()),name='inmunizaciones_crear'),
    url(r'^editar/(?P<pk>\d+)$', login_required(InmunizacionesUpdate.as_view()),name='inmunizaciones_editar'),
    url(r'^eliminar/(?P<pk>\d+)$', login_required(InmunizacionesDelete.as_view()),name='inmunizaciones_eliminar'),

]
