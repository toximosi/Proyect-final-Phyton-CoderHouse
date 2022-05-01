#importaciones------------------
from django import forms 

#code----------------------------
class PostForm (forms.Form):
    titulos = forms.CharField()
    subtitulo = forms.CharField()
    image = forms.CharField()
    cuerpo = forms.CharField()
    autor = forms.CharField()
    fecha = forms.DateField()

class AutorForm (forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()

