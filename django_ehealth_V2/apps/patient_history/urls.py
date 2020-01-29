from django.conf.urls import url

from ..patient_history.views import index_patient

urlpatterns = [
    url(r'^index$', index_patient),
]
