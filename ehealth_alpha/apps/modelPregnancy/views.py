from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from ..modelPregnancy.forms import ModelosPregnancyForm
from ..modelPregnancy.models import Modelos2

import MySQLdb
# Create your views here.
def home(request):
	return render(request, 'index.html')

# custom method for generating predictions
def getPredictions(peso, presion_sistolica, presion_diastolica, pulso_cardiaco, frecuencia_respiratoria, temperatura, pentavalente, difterica, edad, embarazo_previo):
    import pickle
    import theano
    import tensorflow
    import keras
    from keras.models import Sequential
    from keras.models import load_model
    model = load_model('hyp_model.h5')
    scaled = pickle.load(open("scaler.sav", "rb"))
    scaled_files = scaled.transform([[peso, presion_sistolica, presion_diastolica, pulso_cardiaco, frecuencia_respiratoria, temperatura, pentavalente, difterica, edad, embarazo_previo]])
    prediction = model.predict(scaled_files)
    
    return prediction
    """
    if prediction == 0:
        return "not survived"
    elif prediction == 1:
        return "survived"
    else:
        return "error"
    """

# our result page view
"""
def new_business(request):
    if request.method == 'POST':
        post = request.POST.copy() # to make it mutable
        post['diagnostico'] = 1
        post.update({'diagnostico': 1, 'peso': 5000})
        # or set several values from dict
        #post.update({'postvar': 'some_value', 'var': 'value'})
        # or set list
        #post.setlist('list_var', ['some_value', 'other_value']))

        # and update original POST in the end
        request.POST = post
        post.save()


        #form = post
        #if form.is_valid():
            

            # process form data
        return reverse_lazy('ModelosPregnancy:ModelosPregnancy_listar')
            #return render(request, 'directory/new.html', {'resultado': resultado})

    else:
        form = ModelosPregnancyForm()
        context = {
            'form':form,
        }

    #return render(request, 'directory/new.html', {'resultado': resultado})
"""
def result(request):
    post = request.POST.copy()
    post['folio'] = int(request.GET['folio'])
    post['peso'] = int(request.GET['peso'])
    post['presion_sistolica'] = int(request.GET['presion_sistolica'])
    post['presion_diastolica'] = int(request.GET['presion_diastolica'])
    post['pulso_cardiaco'] = int(request.GET['pulso_cardiaco'])
    post['frecuencia_respiratoria'] = int(request.GET['frecuencia_respiratoria'])
    post['temperatura'] = int(request.GET['temperatura'])
    post['pentavalente'] = int(request.GET['pentavalente'])
    post['difterica'] = int(request.GET['difterica'])
    post['edad'] = int(request.GET['edad'])
    post['embarazo_previo'] = int(request.GET['embarazo_previo'])
    post['diagnostico'] =  int(getPredictions(post['peso'], post['presion_sistolica'], post['presion_diastolica'], post['pulso_cardiaco'], post['frecuencia_respiratoria'], post['temperatura'], post['pentavalente'], post['difterica'], post['edad'], post['embarazo_previo']))
    
    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="",  # your password
                     db="ehealth_alpha")        # name of the data base
    cur = db.cursor()

    request.POST = post
    form = ModelosPregnancyForm(request.POST)
    form.save()

    #cur.execute("INSERT INTO `modelpregnancy_modelos2` (folio, peso, presion_sistolica, presion_diastolica, pulso_cardiaco, frecuencia_respiratoria, temperatura, pentavalente, difterica, edad, embarazo_previo) VALUES (%s,%s, %s, %s,%s,%s,%s,%s,%s, %s, %s);",(form['folio'],form['peso'], form['presion_sistolica'], form['presion_diastolica'], form['pulso_cardiaco'], form['frecuencia_respiratoria'], form['temperatura'], form['pentavalente'], form['difterica'], form['edad'], form['embarazo_previo'],form['diagnostico']))
    cur.execute("UPDATE `modelpregnancy_modelos2` SET diagnostico=%s WHERE folio_id=%s;",(post['diagnostico'],post['folio']))
    db.commit()
    db.close()
    """
    request.POST = post
    form = ModelosPregnancyForm(request.POST)
    if form.is_valid():
        form.save()
        return render(request, 'result.html', {'resultado': post['diagnostico']})
        #return render(request, 'result.html', {'resultado': post['diagnostico']})
    """
    return render(request, 'modelPregnancy/modelPregnancy_list.html', {'resultado': 'result'})

class ModelosPregnancyList(ListView):
    model = Modelos2
    template_name= 'modelPregnancy/modelPregnancy_list.html'

class ModelosPregnancyCreate(CreateView):
    model = Modelos2
    form_class = ModelosPregnancyForm
    template_name = 'modelPregnancy/modelPregnancy_form.html'
    success_url = reverse_lazy('ModelosPregnancy:ModelosPregnancy_listar')

class ModelosPregnancyUpdate(UpdateView):
    model = Modelos2
    form_class = ModelosPregnancyForm
    template_name = 'modelPregnancy/modelPregnancy_form.html'
    success_url = reverse_lazy('ModelosPregnancy:ModelosPregnancy_listar')

class ModelosPregnancyDelete(DeleteView):
    model = Modelos2
    template_name = 'modelPregnancy/modelPregnancy_delete.html'
    success_url = reverse_lazy('ModelosPregnancy:ModelosPregnancy_listar')
