
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from ..obstetrical_data.views import DatosObstetricosList, DatosObstetricosCreate, DatosObstetricosDelete, DatosObstetricosUpdate

urlpatterns = [
    #url(r'^index$', index_personal_data, name = 'datos_obstetricos'),
    url(r'^listar$', login_required(DatosObstetricosList.as_view()),name='datos_obstetricos_listar'),
    url(r'^nuevo$', login_required(DatosObstetricosCreate.as_view()),name='datos_obstetricos_crear'),
    url(r'^editar/(?P<pk>\d+)$', login_required(DatosObstetricosUpdate.as_view()),name='datos_obstetricos_editar'),
    url(r'^eliminar/(?P<pk>\d+)$', login_required(DatosObstetricosDelete.as_view()),name='datos_obstetricos_eliminar'),

]
