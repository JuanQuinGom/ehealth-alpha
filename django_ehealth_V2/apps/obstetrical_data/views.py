# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from ..obstetrical_data.forms import DatosObstetricosForm
from ..obstetrical_data.models import Datos_Obstetricos

# Create your views here.
class DatosObstetricosList(ListView):
    model = Datos_Obstetricos
    template_name= 'obstetrical_data/obstetrical_data_list.html'

class DatosObstetricosCreate(CreateView):
    model = Datos_Obstetricos
    form_class = DatosObstetricosForm
    template_name = 'obstetrical_data/obstetrical_data_form.html'
    success_url = reverse_lazy('datos_obstetricos:datos_obstetricos_listar')

class DatosObstetricosUpdate(UpdateView):
    model = Datos_Obstetricos
    form_class = DatosObstetricosForm
    template_name = 'obstetrical_data/obstetrical_data_form.html'
    success_url = reverse_lazy('datos_obstetricos:datos_obstetricos_listar')

class DatosObstetricosDelete(DeleteView):
    model = Datos_Obstetricos
    template_name = 'obstetrical_data/obstetrical_data_delete.html'
    success_url = reverse_lazy('datos_obstetricos:datos_obstetricos_listar')
