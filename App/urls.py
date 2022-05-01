#Importaciones ------------------------------------------------------
from django.urls import path, include
from App import views
from django.contrib.auth.views import LogoutView

#Code ----------------------------------------------------------------
urlpatterns = [

    path("", views.index, name="index"),
    path("autor/", views.autor, name="autor"),
    path("login/", views.login, name="login"),
    path("about/", views.about, name="about"),
    path("error/", views.error, name="error"),
    #post -CRUD-------------------------------------------------------
    path("post/", views.post, name="post"),
    path("post/list/", views.postLV.as_view(), name="list"),
    path(r"^(?P<pk>\d+)$", views.postDV.as_view(), name="detail"),
    path(r"^new$", views.postCV.as_view(), name="new"),
    path(r"^editar/(?P<pk>\d+)$", views.postUV.as_view(), name="edit"),
    path(r"^borrar/<int:pk>/", views.postDeV.as_view(), name="delete"),
    #login -------------------------------------------------------
    path("login", views.login_request, name="login"),
    path("register", views.register, name="register"),
    path("logout", LogoutView.as_view, name="Logout"),
]
