
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from ..consult.views import ConsultasList, ConsultasCreate, ConsultasDelete, ConsultasUpdate

urlpatterns = [
    #url(r'^index$', index_personal_data, name = 'Consultas'),
    url(r'^listar$', login_required(ConsultasList.as_view()),name='consultas_listar'),
    url(r'^nuevo$', login_required(ConsultasCreate.as_view()),name='consultas_crear'),
    url(r'^editar/(?P<pk>\d+)$', login_required(ConsultasUpdate.as_view()),name='consultas_editar'),
    url(r'^eliminar/(?P<pk>\d+)$', login_required(ConsultasDelete.as_view()),name='consultas_eliminar'),

]
