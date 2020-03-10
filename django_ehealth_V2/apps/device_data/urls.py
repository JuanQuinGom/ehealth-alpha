from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from ..device_data.views import DispositivosList, DispositivosCreate, DispositivosDelete, DispositivosUpdate

urlpatterns = [
    #url(r'^index$', index_personal_data, name = 'Dispositivos'),
    url(r'^listar$', login_required(DispositivosList.as_view()),name='dispositivos_listar'),
    url(r'^nuevo$', login_required(DispositivosCreate.as_view()),name='dispositivos_crear'),
    url(r'^editar/(?P<pk>\d+)$', login_required(DispositivosUpdate.as_view()),name='dispositivos_editar'),
    url(r'^eliminar/(?P<pk>\d+)$', login_required(DispositivosDelete.as_view()),name='dispositivos_eliminar'),

]
