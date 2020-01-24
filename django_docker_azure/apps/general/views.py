from django.shortcuts import render,redirect
from django.http import HttpResponse

from ..general.models import Vacunas
from ..general.forms import GeneralForm
# Create your views here.

def index_general(request):
    return render(request,'general/index.html')#render es un acceso directo

def general_view(request):
    #vista basada en funciones
    if request.method == 'POST':
        form = GeneralForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('general:index_g')
    else:
        form = GeneralForm()
    return render(request, 'general/general_form.html',{'form':form})

#def general_list{request}:
#    vacunas = Vacunas.objects.all()
#    contexto = { 'vacunas' : vacunas}
#    return render (request,'general/general_list.html')
