#importaciones------------------
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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


class UserRegisterForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1= forms.CharField(label = "Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Repite la contraseña", widget=forms.PasswordInput)

    class Meta:
            model = User
            fields = ["username", "email", "password1", "password2"]
            help_texts = {k:"" for k in fields}
