"""Sinais do aplicativo usuarios para o marketplace Voltrix."""

from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def criar_superadmin(sender, **kwargs):
    """Cria um superusuário administrativo se ele não existir após migrações."""
    User = get_user_model()
    email = "admin@voltrix.com.br"
    username = "admin"
    senha = "Raioroxo101@"

    if sender.name != "usuarios":
        return

    usuario, criado = User.objects.get_or_create(
        email=email,
        defaults={
            "username": username,
            "nome_completo": "Administrador Voltrix",
            "is_superuser": True,
            "is_staff": True,
            "is_active": True,
            "perfil": "administrador",
        },
    )

    if criado or not usuario.has_usable_password() or not usuario.check_password(senha):
        usuario.username = username
        usuario.is_superuser = True
        usuario.is_staff = True
        usuario.is_active = True
        usuario.perfil = "administrador"
        usuario.set_password(senha)
        usuario.save()
