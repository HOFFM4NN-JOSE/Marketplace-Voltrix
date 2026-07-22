"""URLs do módulo de produtos do Voltrix."""

from django.urls import path

from .views import CategoriaListView, MarcaListView, ProdutoListView

urlpatterns = [
    path("categorias/", CategoriaListView.as_view(), name="lista-categorias"),
    path("marcas/", MarcaListView.as_view(), name="lista-marcas"),
    path("produtos/", ProdutoListView.as_view(), name="lista-produtos"),
]
