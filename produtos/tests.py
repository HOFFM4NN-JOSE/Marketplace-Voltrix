"""Testes para o módulo de produtos do Voltrix."""

from django.test import TestCase

from usuarios.models import Usuario

from .models import Categoria, Marca, Produto


class ProdutoModeloTestes(TestCase):
    """Valida a criação de categorias, marcas e produtos."""

    def test_criar_produto_com_vendedor_e_categoria(self):
        """Um produto deve ser criado com vendedor, categoria e valores válidos."""
        vendedor = Usuario.objects.create_user(
            email="vendedor@voltrix.com.br",
            nome_completo="João Vendedor",
            username="joaovendedor",
            password="SenhaForte123!",
            perfil="vendedor",
        )
        categoria = Categoria.objects.create(
            nome="Eletrônicos", slug="eletronicos", descricao="Produtos eletrônicos"
        )
        marca = Marca.objects.create(nome="Voltrix", slug="voltrix")
        produto = Produto.objects.create(
            vendedor=vendedor,
            categoria=categoria,
            marca=marca,
            titulo="Notebook Voltrix",
            slug="notebook-voltrix",
            sku="VTX-001",
            descricao_curta="Notebook profissional",
            descricao_completa="Notebook para uso profissional",
            preco="3500.00",
            quantidade=10,
            estoque=10,
        )

        self.assertEqual(produto.titulo, "Notebook Voltrix")
        self.assertEqual(produto.vendedor.perfil, "vendedor")
        self.assertEqual(produto.categoria.nome, "Eletrônicos")
