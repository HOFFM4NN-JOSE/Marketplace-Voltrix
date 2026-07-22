"""Modelos para autenticação e perfis do Voltrix."""

from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    """Usuário estendido para suportar perfis de cliente, vendedor e administrador."""

    PERFIS = [
        ("cliente", "Cliente"),
        ("vendedor", "Vendedor"),
        ("administrador", "Administrador"),
    ]

    nome_completo = models.CharField("nome completo", max_length=150)
    email = models.EmailField("e-mail", unique=True)
    telefone = models.CharField("telefone", max_length=20, blank=True)
    whatsapp = models.CharField("whatsapp", max_length=20, blank=True)
    cpf = models.CharField("cpf", max_length=14, blank=True)
    perfil = models.CharField(
        "perfil", max_length=20, choices=PERFIS, default="cliente"
    )
    esta_ativo = models.BooleanField("está ativo", default=True)
    data_criacao = models.DateTimeField("data de criação", auto_now_add=True)
    data_atualizacao = models.DateTimeField("data de atualização", auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "nome_completo"]

    class Meta:
        verbose_name = "usuário"
        verbose_name_plural = "usuários"

    def __str__(self):
        return self.nome_completo or self.email
