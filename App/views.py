#Importaciones ------------------------------------------------------
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from App.models import Post, Autor
from App.forms import Post, Autor

#Code ----------------------------------------------------------------
#*NOTE: la información que se pasa al template
def index(request):
    return render(request, 'index.html')