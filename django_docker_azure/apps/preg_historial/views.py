from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView,CreateView

from ..preg_historial.models import Consultas
from ..personal_data.models import Person
from ..personal_data.forms import PersonForm
from ..preg_historial.forms import ConsultaForm
# Create your views here.

def index_pre(request):
    return HttpResponse("Pregnancy Historial")

class ConsultasList(ListView)
    model = Consultas
    template_name = 'preg_historial/preg_historial_consulta_lista.html'

class ConsultasCreate(CreateView):
    model = Consultas
    template_name = 'preg_historial/preg_historial_consulta_form.html'
    fom_class = PersonForm
    second_form_class = ConsultaForm
    success_url = reverse_lazy('preg_historial:preg_historial_consulta_lista')

    def get_context_data(self, **kwargs):
        context = super(ConsultasCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context
    def post(self,request,*args,**kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            solicitud = form.save(commit=False)
            solicitud.Person = form2.save()
            solicitud.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2= form2))

class ConsultasUpdate(UpdateView):
    model = Consultas
    second_model = Person
    template_name = 'preg_historial/preg_historial_form.html'
    form = ConsultaForm
    second_form_class = PersonForm
    success_url = reverse_lazy('preg_historial:preg_historial_consulta_lista')

    def get_context_data(self,**kwargs):
        context=super(ConsultasUpdate,self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk',0)
        solicitud = self.model.objects.get(id=pk)
        persona = self.second_model.objects.get(id=solicitud.folio)
        #instanciar en formularios
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=persona)
        context['id'] = pk
        return context

    def post(self,request, *args, **kwargs):
        self.object = self.get_object
        id_solicitud = kwargs['pk']
        solicitud = self.model.objects.get(id = id_solicitud)
        persona = self.second_model.objects.get(id = solicitud.folio)
        #sin instancia genera nuevo objeto en lugar de actualizar
        form = self.form_class(request.POST, instance=solicitud)
        form2 = self.second_form_class(request.POST, instance=persona)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())

class ConsultasDelete(DeleteView):
    model = Consultas
    template_name = 'preg_historial/preg_historial_delete.html'
    success_url = reverse_lazy('preg_historial:preg_historial_consulta_lista')
