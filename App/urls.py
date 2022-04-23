#Importaciones ------------------------------------------------------
from django.urls import path, include
from App import views

#Code ----------------------------------------------------------------
urlpatterns = [

    path('', views.index, name='index'),

]
