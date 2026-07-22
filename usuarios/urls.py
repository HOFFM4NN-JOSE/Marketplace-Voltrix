"""URLs do módulo de usuários do Voltrix."""

from django.urls import path

from .views import UsuarioListView

urlpatterns = [
    path("usuarios/", UsuarioListView.as_view(), name="lista-usuarios"),
]
