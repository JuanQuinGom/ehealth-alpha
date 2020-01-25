from django.conf.urls import url
from django,contrib.auth.decorators import login_required
from ..general.views import index_general,general_view
urlpatterns = [
    url(r'^$', login_required(index_general), name = 'index_g'),
    url(r'^nuevo$', login_required(general_view), name = 'generate_vaccine'),
]
