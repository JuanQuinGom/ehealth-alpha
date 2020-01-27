# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from ..personal_data.forms import DatosPersonasForm
from ..personal_data.models import Datos_Personas
# Create your views here.
def index_personal_data(request):
    return render( request, 'personal_data/index.html') # dirigido al template

class DatosPersonasList(ListView):
    model = Datos_Personas
    template_name= 'personal_data/personal_data_list.html'

class DatosPersonasCreate(CreateView):
    model = Datos_Personas
    form_class = DatosPersonasForm
    template_name = 'personal_data/personal_data_form.html'
    success_url = reverse_lazy('datos_personales:datos_personales_listar')

class DatosPersonasUpdate(UpdateView):
    model = Datos_Personas
    form_class = DatosPersonasForm
    template_name = 'personal_data/personal_data_form.html'
    success_url = reverse_lazy('datos_personales:datos_personales_listar')

class DatosPersonasDelete(DeleteView):
    model = Datos_Personas
    template_name = 'personal_data/personal_data_delete.html'
    success_url = reverse_lazy('datos_personales:datos_personales_listar')

def datospersonasedit(request, id_folio):
	folio = Datos_Personas.objects.get(id=id_folio)
	if request.method == 'GET':
		form = DatosPersonasForm(instance=folio)
	else:
		form = DatosPersonasForm(request.POST, instance=folio)
		if form.is_valid():
			form.save()
		return redirect('datos_personales:datos_personales_listar')
	return render(request, 'personal_data/personal_data_form.html', {'form':form})
