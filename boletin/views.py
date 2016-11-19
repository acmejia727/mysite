from django.shortcuts import render
from .forms import RegForm
from .models import Codigo
import sys
from program.chirry import *
from program.chirry_parser import *
from program.chirry_lexer import *
# Create your views here.
error_lex=1

def inicio(request):
    global variable
    global error_lex
    form = RegForm(request.POST or None )
    code=''
    if form.is_valid():
        form_data = form.cleaned_data
        code = form_data.get('codigo')
        name = form_data.get('nombre')
        obj = Codigo.objects.create(codigo=code, nombre=name)

    x=str(code)
    Registro = Codigo.objects.order_by('-timestamp')[:5]
    context = {
        'holamundo':'hola Causa',
        'codigo':'SU CODIGO:',
        'el_form': form,
        'log': main_chirry(x),
        'texto':code,
        'registro':Registro,
        'error_flag': error_parser(),
        'variable':variables(),
    }


    return render(request,'inicio.html',context)
