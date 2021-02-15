"""ehealth_alpha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.views import LoginView, logout_then_login, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    ### Menus de las apps ###
    url(r'^$', include(('apps.homepage.urls','app.homepage'), namespace="principal")),
    url(r'menu/', include(('apps.principal.urls','app.principal'), namespace="menu_2")),
    url(r'^datos_personales/', include(('apps.personal_data.urls','apps.personal_data'), namespace="datos_personales")),
    url(r'^historial_paciente/', include(('apps.patient_history.urls','apps.patient_history'), namespace="historial_paciente")),
    url(r'^enfermedades/', include(('apps.diseases.urls','apps.diseases'), namespace="enfermedades")),
    url(r'^diagnosticos/', include(('apps.diagnosis.urls','apps.diagnosis'), namespace="diagnosticos")),
    url(r'^consultas/', include(('apps.consult.urls','apps.consult'), namespace="consultas")),
    url(r'^dispositivos/', include(('apps.device_data.urls','apps.device_data'), namespace="dispositivos")),
    url(r'^vacunas/', include(('apps.vaccines.urls','apps.vaccines'), namespace="vacunas")),
    url(r'^datos_amarillo/', include(('apps.yellow_data.urls','apps.yellow_data'), namespace="datos_amarillo")),
    url(r'^historial_padre/', include(('apps.father_history.urls','apps.father_history'), namespace="historial_padres")),
    url(r'^historial_madre/', include(('apps.mother_history.urls','apps.mother_history'), namespace="historial_madres")),
    url(r'^datos_obstetricos/', include(('apps.obstetrical_data.urls','apps.obstetrical_data'), namespace="datos_obstetricos")),
    url(r'^inmunizaciones/', include(('apps.inmunizations.urls','apps.inmunizations'), namespace="inmunizaciones")),
    url(r'usuario/', include(('apps.usuario.urls','apps.usuario'), namespace="usuario")),
    url(r'modelo/', views.result, name = "result"))
    #""" Informacion para login y logout """
	url(r'^logout/', logout_then_login, name='logout'),
    url(r'accounts/login/', LoginView.as_view(), name="login"),
    url(r'^reset/password_reset', PasswordResetView.as_view(), {'template_name':'registration/password_reset_form.html',
    'email_template_name':'registration/password_reset_email.html'}, name="password_reset"),
    url(r'^reset/password_reset_done', PasswordResetDoneView.as_view(), {'template_name':'registration/password_reset_done.html'},
     name="password_reset_done"),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(), {'template_name':'registration/password_reset_confirm.html'},
     name="password_reset_confirm"),
    url(r'^reset/done', PasswordResetCompleteView.as_view(), {'template_name':'registration/password_reset_complete.html'},
     name="password_reset_complete"),
]
