"""django_ehealth_V2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', include('apps.homepage.urls', namespace="principal")),
    url(r'^datos_personales/', include('apps.personal_data.urls', namespace="datos_personales")),
    url(r'^historial_paciente/', include('apps.patient_history.urls', namespace="historial_paciente")),
    url(r'^enfermedades/', include('apps.diseases.urls', namespace="enfermedades")),
    url(r'^diagnosticos/', include('apps.diagnosis.urls', namespace="diagnosticos")),
    url(r'^consultas/', include('apps.consult.urls', namespace="consultas")),
    url(r'^dispositivos/', include('apps.device_data.urls', namespace="dispositivos")),
    url(r'^vacunas/', include('apps.vaccines.urls', namespace="vacunas")),
    url(r'^datos_amarillo/', include('apps.yellow_data.urls', namespace="datos_amarillo")),
    url(r'^historial_padre/', include('apps.father_history.urls', namespace="historial_padres")),
    url(r'^historial_madre/', include('apps.mother_history.urls', namespace="historial_madres")),
    url(r'^datos_obstetricos/', include('apps.obstetrical_data.urls', namespace="datos_obstetricos")),
    url(r'^inmunizaciones/', include('apps.inmunizations.urls', namespace="inmunizaciones")),
    url(r'menu/', include('apps.principal.urls', namespace="menu_2")),
    url(r'usuario/', include('apps.usuario.urls', namespace="usuario")),
    url(r'accounts/login/', login, {'template_name':'index.html'} , name="login"),
    url(r'^logout/', logout_then_login, name='logout'),
    url(r'^reset/password_reset', password_reset, {'template_name':'registration/password_reset_form.html',
    'email_template_name':'registration/password_reset_email.html'}, name="password_reset"),
    url(r'^reset/password_reset_done', password_reset_done, {'template_name':'registration/password_reset_done.html'},
     name="password_reset_done"),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm, {'template_name':'registration/password_reset_confirm.html'},
     name="password_reset_confirm"),
    url(r'^reset/done', password_reset_complete, {'template_name':'registration/password_reset_complete.html'},
     name="password_reset_complete"),
]
