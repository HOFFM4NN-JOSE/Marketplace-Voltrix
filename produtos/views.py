"""Views do módulo de produtos do Voltrix."""

from rest_framework import generics

from .models import Categoria, Marca, Produto
from .serializers import CategoriaSerializer, MarcaSerializer, ProdutoSerializer


class CategoriaListView(generics.ListCreateAPIView):
    """Lista e cria categorias do catálogo."""

    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class MarcaListView(generics.ListCreateAPIView):
    """Lista e cria marcas do catálogo."""

    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer


class ProdutoListView(generics.ListCreateAPIView):
    """Lista e cria anúncios de produtos."""

    queryset = Produto.objects.filter(status="ativo")
    serializer_class = ProdutoSerializer
