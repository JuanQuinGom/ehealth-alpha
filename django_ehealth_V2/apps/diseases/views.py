# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from ..diseases.forms import EnfermedadesForm
from ..diseases.models import Enfermedades

# Create your views here.
class EnfermedadesList(ListView):
    model = Enfermedades
    template_name= 'diseases/diseases_list.html'

class EnfermedadesCreate(CreateView):
    model = Enfermedades
    form_class = EnfermedadesForm
    template_name = 'diseases/diseases_form.html'
    success_url = reverse_lazy('enfermedades:enfermedades_listar')

class EnfermedadesUpdate(UpdateView):
    model = Enfermedades
    form_class = EnfermedadesForm
    template_name = 'diseases/diseases_form.html'
    success_url = reverse_lazy('enfermedades:enfermedades_listar')

class EnfermedadesDelete(DeleteView):
    model = Enfermedades
    template_name = 'diseases/diseases_delete.html'
    success_url = reverse_lazy('enfermedades:enfermedades_listar')
