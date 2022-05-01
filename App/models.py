#Importaciones ------------------------------------------------------
from django.db import models

#*NOTE: BASE DE DATOS, El modelo es la parte de nuestro proyecto que almacena, borra, modifica y manipula el caudal principal de los datos
#Models ----------------------------------------------------------------
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=200)
    image = models.CharField(max_length=100)
    cuerpo = models.TextField()
    autor = models.CharField(max_length=100)
    fecha = models.DateField()
    def __str__(self):
        return f"fecha: {self.fecha} - titulos: {self.titulo} - autor: {self.autor}" #para visualizar mejor en bd de admin django

class Autor (models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    def __str__(self):
        return f"Nombre:{self.nombre} - Apellido: {self.apellido}" #para visualizar mejor en bd de admin django