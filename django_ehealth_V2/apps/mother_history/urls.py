from django.conf.urls import url

from ..mother_history.views import Historial_MadresList, Historial_MadresCreate, Historial_MadresDelete, Historial_MadresUpdate

urlpatterns = [
    #url(r'^index$', index_personal_data, name = 'historial_madres'),
    url(r'^listar$', Historial_MadresList.as_view(),name='historial_madres_listar'),
    url(r'^nuevo$', Historial_MadresCreate.as_view(),name='historial_madres_crear'),
    url(r'^editar/(?P<pk>\d+)$', Historial_MadresUpdate.as_view(),name='historial_madres_editar'),
    url(r'^eliminar/(?P<pk>\d+)$', Historial_MadresDelete.as_view(),name='historial_madres_eliminar'),

]
