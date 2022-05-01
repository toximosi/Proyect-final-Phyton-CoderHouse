#Importaciones ------------------------------------------------------
from dataclasses import fields
from multiprocessing import context
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from App.models import Post, Autor
from App.forms import PostForm, AutorForm
#importaciones LISVIEW - Clases Basadas en Vistas - CRUD ----------------
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy





#Code -------------------------------------------------------------------
#Vistas simples----------------------------------------------------------
#*NOTE: la información que se pasa al template
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'App/section/login.html')

def signup(request):
    return render(request, 'App/section/signup.html')

def profile(request):
    return render(request, 'App/section/profile/profile.html')

def mesages(request):
    return render(request, 'App/section/mesages.html')

def about(request):
    return render(request, 'App/section/about.html')

def error(request):
    return render(request, 'App/section/404.html')

#!POST----------------------------------------------------------
def post(request):
    return render(request, 'section/post/post.html')
#
# *CRUD: CBV -- mediante DJANGO ------------------------------------------------------------------
class postLV(ListView):
    model = Post
    template_name = "section/post/post_list.html"

# Read: Lectura ----------------------------------
class postDV(DetailView):
    model = Post
    template_name = "section/post/post_detail.html"

# Create: Crear ----------------------------------
class postCV(CreateView):
    model = Post
    success_url = "/post/list"
    fields = ["titulo", "subtitulo", "image", "cuerpo", "autor", "fecha"]

# Delete: Borrar --------------------------------------
class postDeV(DeleteView):
    model = Post
    template_name = "section/post/post_confirm_delete.html"
    success_url = "/post/list"

# Update: Actualizar ----------------------------------
class postUV(UpdateView):
    model = Post
    template_name = "section/post/post_form.html"
    sucess_url = "/App/post/list"
    fields = ["titulo", "subtitulo", "image", "cuerpo", "autor", "fecha"]

#!Autores----------------------------------------------------------
#*CRUD -- mediante PYTHON ------------------------------------------------------------------
# Read: Lectura ----------------------------------
def autor(request):
    autor = Autor.objects.all() #Trae todos los autores
    ctxt = { "autor" : autor} #guardamos datos
    return render (request, "section/autor.html", ctxt) #Enviamos datos a la vista html

# Create: Crear ----------------------------------
def autorCreate(request):
    if request.method == "POST":
        myForm = AutorForm(request.POST)#recibimos la información del html
        if myForm.is_valid:
            info = myForm.cleaned_data
            autor = Autor (nombre = info["nombre"], apellido = info["apellido"])
            autor.save()
            return render(request, "App/section/autor.html")#redirigo la web a donde quiera
    else:
        miFormulario = AutorForm()#Formulario vacio para construir el html
    return render(request, "App/section/autor.html", {"myForm":myForm})

# Delete: Borrar --------------------------------------
def autorDelete(request, idF):
    autor = Autor.objects.get(id=idF)
    autor.delete()
    #vuelvo al menu
    ctxt = {"autor":autor}
    return render(request, "section/autor.html",ctxt)

# Update: Actualizar ----------------------------------
def autorUpdate(request, idF):
    autor = Autor.objects.get(id = idF)

    if request.method=="POST":
        myForm = AutorForm(request.POST)
        if myForm.is_valid:
            info=myForm.cleaned_data

            autor.nombre = info['nombre']
            autor.apellido = info['apellido']

            autor.save()
            return render(request, "App/section/autor.html")
    else:
        myForm=AutorForm( initial = {"nombre":autor.nombre, "apellido":autor.apellido})
    return render(request,"App/section/autor.html", {"myForm":myForm, "autor_id":idF })

""" def autorResultados(request):
    if request.GET["fname"]:
        nombre =request.GET['fname']
        estudiantes = Autor.objects.filter(nombre__icontains=nombre)
        return render(request, "App/autor.html", {"autor":autor, "query":nombre })
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta) """

""" def autorBuscador(request):
    return render(request, "App/autor.html",) """

""" def autorFormulario(request):
    if request.method == 'POST':
        miFormulario = AutorFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            autor = Autor(nombre=informacion['nombre'], apellido = informacion['apellido'],)
            autor.save()
            return render(request,"estudiantes.html")
    else:
        miFormulario = autorFormulario()
    return render(request,"autorFormulario.html", {"miFormulario":miFormulario}) """