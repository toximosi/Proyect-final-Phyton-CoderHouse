#Importaciones ------------------------------------------------------
from django.db import models

#*NOTE: BASE DE DATOS, El modelo es la parte de nuestro proyecto que almacena, borra, modifica y manipula el caudal principal de los datos
#Models ----------------------------------------------------------------
class Post(models.Model):
    Titulos = models.CharField(max_length=100)
    subtitulo = models.CharField()
    image = models.CharField()
    cuerpo = models.CharField()
    autor = models.CharField()
    fecha = models.DateField()

class Autor (models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)