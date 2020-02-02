# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from ..device.forms import DispositivosForm
from ..device.models import Dispositivos

# Create your views here.
class DispositivosList(ListView):
    model = Dispositivos
    template_name= 'device/device_list.html'

class DispositivosCreate(CreateView):
    model = Dispositivos
    form_class = DispositivosForm
    template_name = 'device/device_form.html'
    success_url = reverse_lazy('dispositivos:dispositivos_listar')

class DispositivosUpdate(UpdateView):
    model = Dispositivos
    form_class = DispositivosForm
    template_name = 'device/device_form.html'
    success_url = reverse_lazy('dispositivos:dispositivos_listar')

class DispositivosDelete(DeleteView):
    model = Dispositivos
    template_name = 'device/device_delete.html'
    success_url = reverse_lazy('dispositivos:dispositivos_listar')
