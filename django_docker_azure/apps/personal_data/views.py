from django.shortcuts import render
from django.http import HttpResponse

from ..personal_data.models import Person # para lista

# Create your views here.

def index_personal(request):
    return HttpResponse("personal data")

def personal_list(request):
    personal = Person.objects.all()
    contexto= {'personal': personal}
    return render (request, 'personal_data/personal_data_list.html',contexto)

def personal_edit(request, id_personal):
    personal = Person.objects.get(id_personal=folio) # obtener el archivo
    if request.method == 'GET':
        form =
