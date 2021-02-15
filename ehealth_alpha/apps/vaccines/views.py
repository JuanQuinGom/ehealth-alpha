# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from ..vaccines.forms import VacunacionesForm
from ..vaccines.models import Vacunaciones

# Create your views here.
class VacunacionesList(ListView):
    model = Vacunaciones
    template_name= 'vaccines/vaccines_list.html'

class VacunacionesCreate(CreateView):
    model = Vacunaciones
    form_class = VacunacionesForm
    template_name = 'vaccines/vaccines_form.html'
    success_url = reverse_lazy('vacunas:vacunas_listar')

class VacunacionesUpdate(UpdateView):
    model = Vacunaciones
    form_class = VacunacionesForm
    template_name = 'vaccines/vaccines_form.html'
    success_url = reverse_lazy('vacunas:vacunas_listar')

class VacunacionesDelete(DeleteView):
    model = Vacunaciones
    template_name = 'vaccines/vaccines_delete.html'
    success_url = reverse_lazy('vacunas:vacunas_listar')
