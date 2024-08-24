from django.shortcuts import render
from django.http import HttpResponse
from .models import * # importamos los modelos

# Create your views here.
def saludo(request):  #creo una funcion que me responda un hola mundo en una pagina html
    return HttpResponse('Hola mundo') 