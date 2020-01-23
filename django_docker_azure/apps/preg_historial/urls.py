from django.conf.urls import url
from ..preg_historial.views import index_pre
urlpatterns = [
    url(r'^$', index_pre),
]
