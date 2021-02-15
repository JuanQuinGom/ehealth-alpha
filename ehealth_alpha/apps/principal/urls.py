
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    #url(r'^index$', index_personal_data, name = 'historial_padres'),
    url(r'^$', login_required(views.nombre),name='menu_principal'),
]
