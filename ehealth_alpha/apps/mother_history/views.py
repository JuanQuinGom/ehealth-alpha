# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from ..mother_history.forms import HistorialMadresForm
from ..mother_history.models import Historial_Madres

# Create your views here.
class Historial_MadresList(ListView):
    model = Historial_Madres
    template_name= 'mother_history/mother_history_list.html'

class Historial_MadresCreate(CreateView):
    model = Historial_Madres
    form_class = HistorialMadresForm
    template_name = 'mother_history/mother_history_form.html'
    success_url = reverse_lazy('historial_madres:historial_madres_listar')

class Historial_MadresUpdate(UpdateView):
    model = Historial_Madres
    form_class = HistorialMadresForm
    template_name = 'mother_history/mother_history_form.html'
    success_url = reverse_lazy('historial_madres:historial_madres_listar')

class Historial_MadresDelete(DeleteView):
    model = Historial_Madres
    template_name = 'mother_history/mother_history_delete.html'
    success_url = reverse_lazy('historial_madres:historial_madres_listar')
