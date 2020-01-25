from django.conf.urls import url
from ..preg_historial.views import index_pre
urlpatterns = [
    url(r'^$', index_pre),
    url(r'^/preg_historial/consulta/consulta_nueva$',ConsultasCreate.as_view(), name = 'consulta_generar'),
    url(r'^/preg_historial/consulta/consulta_update/(?P<pk>\d+)$',ConsultasUpdate.as_view(), name = 'consulta_actualizar'),
    url(r'^/preg_historial/consulta/consulta_eliminar/(?P<pk>\d+)$',ConsultasDelete.as_view(), name = 'consulta_eliminar'),
]
