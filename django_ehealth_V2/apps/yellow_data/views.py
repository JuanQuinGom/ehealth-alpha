# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from ..yellow_data.forms import DatosAmarilloForm
from ..yellow_data.models import Datos_Amarillo

# Create your views here.
class DatosAmarilloList(ListView):
    model = Datos_Amarillo
    template_name= 'yellow_data/yellow_data_list.html'

class DatosAmarilloCreate(CreateView):
    model = Datos_Amarillo
    form_class = DatosAmarilloForm
    template_name = 'yellow_data/yellow_data_form.html'
    success_url = reverse_lazy('datos_amarillo:datos_amarillo_listar')

class DatosAmarilloUpdate(UpdateView):
    model = Datos_Amarillo
    form_class = DatosAmarilloForm
    template_name = 'yellow_data/yellow_data_form.html'
    success_url = reverse_lazy('datos_amarillo:datos_amarillo_listar')

class DatosAmarilloDelete(DeleteView):
    model = Datos_Amarillo
    template_name = 'yellow_data/yellow_data_delete.html'
    success_url = reverse_lazy('datos_amarillo:datos_amarillo_listar')
