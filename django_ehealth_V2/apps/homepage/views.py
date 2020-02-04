# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'homepage/homepage.html'
    )
