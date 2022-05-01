#Importaciones ------------------------------------------------------
from django.contrib import admin
from django.urls import path, include

#Code ----------------------------------------------------------------
urlpatterns = [
    path('admin/', admin.site.urls),
    #vistas-------------------------------------
    path('', include('App.urls')),
]
