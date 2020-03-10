
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from ..yellow_data.views import DatosAmarilloList, DatosAmarilloCreate, DatosAmarilloDelete, DatosAmarilloUpdate

urlpatterns = [
    #url(r'^index$', index_personal_data, name = 'datos_amarillo'),
    url(r'^listar$', login_required(DatosAmarilloList.as_view()),name='datos_amarillo_listar'),
    url(r'^nuevo$', login_required(DatosAmarilloCreate.as_view()),name='datos_amarillo_crear'),
    url(r'^editar/(?P<pk>\d+)$', login_required(DatosAmarilloUpdate.as_view()),name='datos_amarillo_editar'),
    url(r'^eliminar/(?P<pk>\d+)$', login_required(DatosAmarilloDelete.as_view()),name='datos_amarillo_eliminar'),

]
