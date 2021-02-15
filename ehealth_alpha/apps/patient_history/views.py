# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from ..patient_history.forms import HistorialPacienteForm
from ..patient_history.models import Historial_Paciente

# Create your views here.
def index_patient(request):
    return HttpResponse("Index de patient_history")

class HistorialPacienteList (ListView):
    model = Historial_Paciente
    template_name = 'patient_history/patient_history_list.html'

class HistorialPacienteCreate(CreateView):
    model = Historial_Paciente
    form_class = HistorialPacienteForm
    template_name = 'patient_history/patient_history_form.html'
    success_url = reverse_lazy('historial_paciente:historial_paciente_listar')

class HistorialPacienteUpdate(UpdateView):
    model = Historial_Paciente
    form_class = HistorialPacienteForm
    template_name  = 'patient_history/patient_history_form.html'
    success_url = reverse_lazy('historial_paciente:historial_paciente_listar')

class HistorialPacienteDelete(DeleteView):
    model = Historial_Paciente
    template_name = 'patient_history/patient_history_delete.html'
    success_url = reverse_lazy ('historial_paciente:historial_paciente_listar')
