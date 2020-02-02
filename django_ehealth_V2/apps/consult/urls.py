
from django.conf.urls import url

from ..consult.views import ConsultasList, ConsultasCreate, ConsultasDelete, ConsultasUpdate

urlpatterns = [
    #url(r'^index$', index_personal_data, name = 'Consultas'),
    url(r'^listar$', ConsultasList.as_view(),name='consultas_listar'),
    url(r'^nuevo$', ConsultasCreate.as_view(),name='consultas_crear'),
    url(r'^editar/(?P<pk>\d+)$', ConsultasUpdate.as_view(),name='consultas_editar'),
    url(r'^eliminar/(?P<pk>\d+)$', ConsultasDelete.as_view(),name='consultas_eliminar'),

]
