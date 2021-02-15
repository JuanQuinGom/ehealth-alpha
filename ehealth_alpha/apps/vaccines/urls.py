
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from ..vaccines.views import VacunacionesList, VacunacionesCreate, VacunacionesDelete, VacunacionesUpdate

urlpatterns = [
    #url(r'^index$', index_personal_data, name = 'vacunas'),
    url(r'^listar$', login_required(VacunacionesList.as_view()),name='vacunas_listar'),
    url(r'^nuevo$', login_required(VacunacionesCreate.as_view()),name='vacunas_crear'),
    url(r'^editar/(?P<pk>\d+)$', login_required(VacunacionesUpdate.as_view()),name='vacunas_editar'),
    url(r'^eliminar/(?P<pk>\d+)$', login_required(VacunacionesDelete.as_view()),name='vacunas_eliminar'),

]
