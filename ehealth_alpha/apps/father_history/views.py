# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from ..father_history.forms import HistorialPadresForm
from ..father_history.models import Historial_Padres

# Create your views here.
class Historial_PadresList(ListView):
    model = Historial_Padres
    template_name= 'father_history/father_history_list.html'

class Historial_PadresCreate(CreateView):
    model = Historial_Padres
    form_class = HistorialPadresForm
    template_name = 'father_history/father_history_form.html'
    success_url = reverse_lazy('historial_padres:historial_padres_listar')

class Historial_PadresUpdate(UpdateView):
    model = Historial_Padres
    form_class = HistorialPadresForm
    template_name = 'father_history/father_history_form.html'
    success_url = reverse_lazy('historial_padres:historial_padres_listar')

class Historial_PadresDelete(DeleteView):
    model = Historial_Padres
    template_name = 'father_history/father_history_delete.html'
    success_url = reverse_lazy('historial_padres:historial_padres_listar')
