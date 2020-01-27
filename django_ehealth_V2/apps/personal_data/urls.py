from django.conf.urls import url

from ..personal_data.views import index_personal_data, DatosPersonasList, DatosPersonasCreate, DatosPersonasUpdate, DatosPersonasDelete, datospersonasedit

urlpatterns = [
    url(r'^index$', index_personal_data, name = 'datos_personales'),
    url(r'^listar$', DatosPersonasList.as_view(),name='datos_personales_listar'),
    url(r'^nuevo$', DatosPersonasCreate.as_view(),name='datos_personales_crear'),
    url(r'^editar/(?P<pk>\d+)$', DatosPersonasUpdate.as_view(),name='datos_personales_editar'),
    url(r'^eliminar/(?P<pk>\d+)$', DatosPersonasDelete.as_view(),name='datos_personales_eliminar'),

]
