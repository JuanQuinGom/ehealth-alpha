from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from ..modelPregnancy.views import getPredictions, result
from ..modelPregnancy.views import ModelosPregnancyList,ModelosPregnancyCreate,ModelosPregnancyDelete,ModelosPregnancyUpdate
from django.urls import path

urlpatterns = [
    #url(r'^index$', index_patient),
    #url(r'^/resultado', new_business, name = "resultado"),
    #url(r'^$', home, name='modelAI'),
    url(r'^result/', result, name='result'),
    url(r'^listar$', login_required(ModelosPregnancyList.as_view()),name='ModelosPregnancy_listar'),
    url(r'^nuevo$', login_required(ModelosPregnancyCreate.as_view()),name='ModelosPregnancy_crear'),
    url(r'^editar/(?P<pk>\d+)$', login_required(ModelosPregnancyUpdate.as_view()),name='ModelosPregnancy_editar'),
    url(r'^eliminar/(?P<pk>\d+)$', login_required(ModelosPregnancyDelete.as_view()),name='ModelosPregnancy_eliminar'),
    
]
