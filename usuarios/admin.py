"""Configuração administrativa para o módulo de usuários."""

from django.contrib import admin

from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    """Administração do modelo de usuário."""

    list_display = ("nome_completo", "email", "perfil", "esta_ativo")
    search_fields = ("nome_completo", "email", "cpf")
    list_filter = ("perfil", "esta_ativo")
