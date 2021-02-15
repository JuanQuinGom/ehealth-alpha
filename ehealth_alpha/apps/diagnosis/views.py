# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from ..diagnosis.forms import DiagnosticosForm
from ..diagnosis.models import Diagnosticos

# Create your views here.
class DiagnosticosList (ListView):
    model = Diagnosticos
    template_name = 'diagnosis/diagnosis_list.html'

class DiagnosticosCreate(CreateView):
    model = Diagnosticos
    form_class = DiagnosticosForm
    template_name = 'diagnosis/diagnosis_form.html'
    success_url = reverse_lazy('diagnosticos:diagnosticos_listar')

class DiagnosticosUpdate(UpdateView):
    model = Diagnosticos
    form_class = DiagnosticosForm
    template_name  = 'diagnosis/diagnosis_form.html'
    success_url = reverse_lazy('diagnosticos:diagnosticos_listar')

class DiagnosticosDelete(DeleteView):
    model = Diagnosticos
    template_name = 'diagnosis/diagnosis_delete.html'
    success_url = reverse_lazy ('diagnosticos:diagnosticos_listar')
