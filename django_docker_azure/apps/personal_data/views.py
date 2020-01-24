from django.shortcuts import render
from django.http import HttpResponse

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
