# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from ..consult.forms import ConsultasForm
from ..consult.models import Consultas

# Create your views here.
class ConsultasList(ListView):
    model = Consultas
    template_name= 'consults/consults_list.html'

class ConsultasCreate(CreateView):
    model = Consultas
    form_class = ConsultasForm
    template_name = 'consults/consults_form.html'
    success_url = reverse_lazy('consultas:consultas_listar')

class ConsultasUpdate(UpdateView):
    model = Consultas
    form_class = ConsultasForm
    template_name = 'consults/consults_form.html'
    success_url = reverse_lazy('consultas:consultas_listar')

class ConsultasDelete(DeleteView):
    model = Consultas
    template_name = 'consults/consults_delete.html'
    success_url = reverse_lazy('consultas:consultas_listar')
