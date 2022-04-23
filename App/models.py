#Importaciones ------------------------------------------------------
from django.db import models

#*NOTE: BASE DE DATOS, El modelo es la parte de nuestro proyecto que almacena, borra, modifica y manipula el caudal principal de los datos
#Models ----------------------------------------------------------------
class Post(models.Model):
    Titulos = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=200)
    image = models.CharField(max_length=100)
    cuerpo = models.TextField()
    autor = models.CharField(max_length=100)
    fecha = models.DateField()

class Autor (models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)