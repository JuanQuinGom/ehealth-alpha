from django.conf.urls import url
from ..personal_data.views import index_personal,personal_list,personal_view,personal_edit

urlpatterns = [
    url(r'^$', index_personal),
    url(r'^nuevo$', personal_view, name = 'generate_personal_data'),
    url(r'^listar$',personal_list, name='personal_data_list'),
    url(r'^editar/(?P<folio>\d+)$',personal_edit, name='personal_data_edit'),
]
