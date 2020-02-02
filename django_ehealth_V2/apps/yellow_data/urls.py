
from django.conf.urls import url

from ..yellow_data.views import DatosAmarilloList, DatosAmarilloCreate, DatosAmarilloDelete, DatosAmarilloUpdate

urlpatterns = [
    #url(r'^index$', index_personal_data, name = 'datos_amarillo'),
    url(r'^listar$', DatosAmarilloList.as_view(),name='datos_amarillo_listar'),
    url(r'^nuevo$', DatosAmarilloCreate.as_view(),name='datos_amarillo_crear'),
    url(r'^editar/(?P<pk>\d+)$', DatosAmarilloUpdate.as_view(),name='datos_amarillo_editar'),
    url(r'^eliminar/(?P<pk>\d+)$', DatosAmarilloDelete.as_view(),name='datos_amarillo_eliminar'),

]
