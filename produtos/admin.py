"""Configuração administrativa para os modelos de produtos do Voltrix."""

from django.contrib import admin

from .models import Categoria, Marca, Produto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    """Administração das categorias do catálogo."""

    list_display = ("nome", "slug")
    search_fields = ("nome",)


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    """Administração das marcas do catálogo."""

    list_display = ("nome", "slug")
    search_fields = ("nome",)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    """Administração dos anúncios de produtos."""

    list_display = ("titulo", "vendedor", "categoria", "status", "preco")
    list_filter = ("status", "condicao")
    search_fields = ("titulo", "sku")
