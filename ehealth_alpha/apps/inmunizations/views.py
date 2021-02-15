# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from ..inmunizations.forms import InmunizacionesForm
from ..inmunizations.models import Inmunizaciones

# Create your views here.
class InmunizacionesList(ListView):
    model = Inmunizaciones
    template_name= 'inmunizations/inmunizations_list.html'

class InmunizacionesCreate(CreateView):
    model = Inmunizaciones
    form_class = InmunizacionesForm
    template_name = 'inmunizations/inmunizations_form.html'
    success_url = reverse_lazy('inmunizaciones:inmunizaciones_listar')

class InmunizacionesUpdate(UpdateView):
    model = Inmunizaciones
    form_class = InmunizacionesForm
    template_name = 'inmunizations/inmunizations_form.html'
    success_url = reverse_lazy('inmunizaciones:inmunizaciones_listar')

class InmunizacionesDelete(DeleteView):
    model = Inmunizaciones
    template_name = 'inmunizations/inmunizations_delete.html'
    success_url = reverse_lazy('inmunizaciones:inmunizaciones_listar')
