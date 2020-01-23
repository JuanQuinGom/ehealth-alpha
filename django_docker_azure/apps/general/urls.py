from django.conf.urls import url

from ..general.views import index_general,general_view
urlpatterns = [
    url(r'^$', index_general, name = 'index_g'),
    url(r'^nuevo$', general_view, name = 'generate_vaccine'),
]
