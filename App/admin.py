#importaciones----------------------------
from django.contrib import admin
from .models import *

# Register your models here.
#Code---------------------------------
admin.site.register(Post)
admin.site.register(Autor)