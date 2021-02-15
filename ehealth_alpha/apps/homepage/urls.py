
from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^index$', index_personal_data, name = 'historial_padres'),
    url(r'^$', views.index,name='principal'),
]
