"""Serializadores do módulo de usuários do Voltrix."""

from rest_framework import serializers

from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    """Serializador para exposição pública de dados do usuário."""

    class Meta:
        model = Usuario
        fields = ("id", "nome_completo", "email", "perfil", "telefone", "whatsapp")
