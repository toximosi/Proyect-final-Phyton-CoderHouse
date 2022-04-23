#importaciones------------------
from django import forms 

#code----------------------------
class Post(forms.Form):
    titulos = forms.CharField()
    subtitulo = forms.CharField()
    image = forms.CharField()
    cuerpo = forms.CharField()
    autor = forms.CharField()
    fecha = forms.DateField()

class Autor (forms.Model):
    nombre = forms.CharField()
    apellido = forms.CharField()

