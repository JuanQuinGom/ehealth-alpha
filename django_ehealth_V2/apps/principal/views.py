# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def nombre(request):
    """
    Función vista a la pagina menu_principal del sitio.
    """
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'principal/menu.html'
    )
