from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from ..personal_data.views import index_personal_data, DatosPersonasList, DatosPersonasCreate, DatosPersonasUpdate, DatosPersonasDelete, datospersonasedit

urlpatterns = [
    url(r'^index$', login_required(index_personal_data), name = 'datos_personales'),
    url(r'^listar$', login_required(DatosPersonasList.as_view()),name='datos_personales_listar'),
    url(r'^nuevo$', login_required(DatosPersonasCreate.as_view()),name='datos_personales_crear'),
    url(r'^editar/(?P<pk>\d+)$', login_required(DatosPersonasUpdate.as_view()),name='datos_personales_editar'),
    url(r'^eliminar/(?P<pk>\d+)$', login_required(DatosPersonasDelete.as_view()),name='datos_personales_eliminar'),

]
