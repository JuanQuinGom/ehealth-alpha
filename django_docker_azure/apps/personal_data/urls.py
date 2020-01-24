from django.conf.urls import url
from ..personal_data.views import index_personal,personal_list,personal_view,personal_edit,personal_delete, PersonaList, PersonaCreate, PersonaUpdate, PersonaDelete


urlpatterns = [
    url(r'^$', index_personal),
    url(r'^nuevo$', PersonaCreate.as_view(), name = 'generate_personal_data'),
    url(r'^listar$',PersonaList.as_view(), name='personal_data_list')
    url(r'^editar/(?P<pk>\d+)$',PersonaUpdate.as_view(), name='personal_data_edit'),
    url(r'^eliminar/(?P<pk>\d+)$',PersonaDelete.as_view(), name='personal_data_delete'),
]
