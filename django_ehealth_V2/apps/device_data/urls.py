from django.conf.urls import url

from ..device_data.views import DispositivosList, DispositivosCreate, DispositivosDelete, DispositivosUpdate

urlpatterns = [
    #url(r'^index$', index_personal_data, name = 'Dispositivos'),
    url(r'^listar$', DispositivosList.as_view(),name='dispositivos_listar'),
    url(r'^nuevo$', DispositivosCreate.as_view(),name='dispositivos_crear'),
    url(r'^editar/(?P<pk>\d+)$', DispositivosUpdate.as_view(),name='dispositivos_editar'),
    url(r'^eliminar/(?P<pk>\d+)$', DispositivosDelete.as_view(),name='dispositivos_eliminar'),

]
