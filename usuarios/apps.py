"""Configuração do aplicativo de usuários do Voltrix."""

from django.apps import AppConfig


class UsuariosConfig(AppConfig):
    """Configuração do módulo de autenticação e perfis."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "usuarios"
    verbose_name = "Usuários"

    def ready(self):
        # Importa os sinais do aplicativo.
        # Garante que o superadmin seja criado após as migrações.
        from . import signals  # noqa: F401
