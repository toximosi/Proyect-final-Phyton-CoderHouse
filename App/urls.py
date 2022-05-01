#Importaciones ------------------------------------------------------
from django.urls import path, include
from App import views

#Code ----------------------------------------------------------------
urlpatterns = [

    path('', views.index, name='index'),
    path('autor/', views.autor, name='autor'),
    path('post/', views.post, name='post'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('error/', views.error, name='error'),

]
