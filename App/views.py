#Importaciones ------------------------------------------------------
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from App.django.forms import Post, Autor
from App.django.models import Post, Autor

#Code ----------------------------------------------------------------
#*NOTE: la información que se pasa al template
def pag(request):
    return render(request, 'parent.html')