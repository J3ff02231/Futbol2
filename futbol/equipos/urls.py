from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_equipos, name="lista_equipos"),
    path("crear/", views.crear_equipo, name="crear_equipo"),
]
