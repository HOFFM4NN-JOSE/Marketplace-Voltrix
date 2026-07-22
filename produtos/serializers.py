"""Serializadores do módulo de produtos do Voltrix."""

from rest_framework import serializers

from .models import Categoria, Marca, Produto


class CategoriaSerializer(serializers.ModelSerializer):
    """Serializador para categorias do catálogo."""

    class Meta:
        model = Categoria
        fields = ("id", "nome", "slug", "descricao")


class MarcaSerializer(serializers.ModelSerializer):
    """Serializador para marcas do catálogo."""

    class Meta:
        model = Marca
        fields = ("id", "nome", "slug")


class ProdutoSerializer(serializers.ModelSerializer):
    """Serializador para anúncios de produtos."""

    class Meta:
        model = Produto
        fields = (
            "id",
            "titulo",
            "slug",
            "sku",
            "preco",
            "status",
            "categoria",
            "marca",
        )
