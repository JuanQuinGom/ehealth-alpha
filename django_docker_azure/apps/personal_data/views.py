from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from ..personal_data.models import Person # para lista
from ..personal_data.forms import PersonForm
# Create your views here.

def index_personal(request):
    return HttpResponse("personal data")

def personal_list(request):
    personal = Person.objects.all()
    contexto= {'personal': personal}
    return render (request, 'personal_data/personal_data_list.html',contexto)

def personal_view(request):
    #vista basada en funciones
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('personal:index_g')
    else:
        form = PersonForm()
    return render(request, 'personal_data/personal_data_form.html',{'form':form})


def personal_edit(request, folio):
    personal = Person.objects.get(id=folio) # obtener el archivo
    if request.method == 'GET':
        form = PersonForm(instance=personal)
    else:
        form = PersonForm(request.POST, instance=personal)
        if form.is_valid():
            form.save()
        return redirect('personal_data:personal_data_list')
    return render(request,'personal_data/personal_data_form.html',{'form' : form})

def personal_delete(request, folio):
    personal = Person.objects.get(id=folio)
    if request.method == 'POST':
        personal.delete()
        return redirect('persona_data/personal_data_list')
    return render(request, 'personal_data/personal_data_delete.html',{'personal_data':personal})


#vista basada en clases
class PersonaList(ListView):
    model = Person
    template_name = 'personal_data/personal_data_list.html'

class PersonaCreate(CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'personal_data/personal_data_form.html'
    success_url = reverse_lazy('personal_data:personal_data_list')

class PersonaUpdate(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'personal_data/personal_data_form.html'
    success_url = reverse_lazy('personal_data:personal_data_list')

class PersonaDelete(DeleteView):
    model = Person
    template_name = 'personal_data/personal_data_form.html'
    success_url = reverse_lazy('personal_data:personal_data_list')
