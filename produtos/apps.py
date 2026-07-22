"""Configuração do aplicativo de produtos do Voltrix."""

from django.apps import AppConfig


class ProdutosConfig(AppConfig):
    """Configuração do módulo de catálogo e anúncios."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "produtos"
    verbose_name = "Produtos"
