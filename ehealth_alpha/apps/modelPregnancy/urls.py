from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from ..modelPregnancy.views import home, getPredictions, result

urlpatterns = [
    #url(r'^index$', index_patient),
    url(r'^/resultado', result, name = "resultado"),
    url(r'^$', home, name='home'),
    
]
