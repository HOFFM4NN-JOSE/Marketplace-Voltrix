"""Testes iniciais para o módulo de usuários do Voltrix."""

from django.test import TestCase

from usuarios.models import Usuario


class UsuarioModeloTestes(TestCase):
    """Garante que o modelo de usuário suporta cadastro profissional."""

    def test_criar_usuario_com_email_e_perfil(self):
        """Um usuário deve ser criado com email, nome e perfil válidos."""
        usuario = Usuario.objects.create_user(
            email="cliente@voltrix.com.br",
            nome_completo="Maria Souza",
            username="mariasouza",
            password="SenhaForte123!",
            perfil="cliente",
        )

        self.assertEqual(usuario.email, "cliente@voltrix.com.br")
        self.assertTrue(usuario.check_password("SenhaForte123!"))
        self.assertEqual(usuario.perfil, "cliente")
