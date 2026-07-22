"""Modelos de categoria, marca e produto para o marketplace Voltrix."""

from django.db import models

from usuarios.models import Usuario


class Categoria(models.Model):
    """Categoria principal do catálogo."""

    nome = models.CharField("nome", max_length=100, unique=True)
    slug = models.SlugField("slug", unique=True)
    descricao = models.TextField("descrição", blank=True)
    data_criacao = models.DateTimeField("data de criação", auto_now_add=True)

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.nome


class Marca(models.Model):
    """Marca do produto."""

    nome = models.CharField("nome", max_length=100, unique=True)
    slug = models.SlugField("slug", unique=True)
    data_criacao = models.DateTimeField("data de criação", auto_now_add=True)

    class Meta:
        verbose_name = "marca"
        verbose_name_plural = "marcas"

    def __str__(self):
        return self.nome


class Produto(models.Model):
    """Anúncio de produto disponível para venda no marketplace."""

    CONDICOES = [
        ("novo", "Novo"),
        ("usado", "Usado"),
    ]

    STATUS = [
        ("rascunho", "Rascunho"),
        ("ativo", "Ativo"),
        ("pausado", "Pausado"),
    ]

    vendedor = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, related_name="produtos"
    )
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="produtos"
    )
    marca = models.ForeignKey(
        Marca, on_delete=models.PROTECT, related_name="produtos", blank=True, null=True
    )
    titulo = models.CharField("título", max_length=200)
    slug = models.SlugField("slug", unique=True)
    sku = models.CharField("SKU", max_length=100, unique=True)
    descricao_curta = models.CharField("descrição curta", max_length=255)
    descricao_completa = models.TextField("descrição completa")
    preco = models.DecimalField("preço", max_digits=10, decimal_places=2)
    preco_promocional = models.DecimalField(
        "preço promocional", max_digits=10, decimal_places=2, blank=True, null=True
    )
    quantidade = models.PositiveIntegerField("quantidade em estoque", default=1)
    peso = models.DecimalField("peso", max_digits=8, decimal_places=3, default=0)
    altura = models.DecimalField("altura", max_digits=6, decimal_places=2, default=0)
    largura = models.DecimalField("largura", max_digits=6, decimal_places=2, default=0)
    comprimento = models.DecimalField(
        "comprimento", max_digits=6, decimal_places=2, default=0
    )
    garantia = models.PositiveIntegerField("garantia", default=0)
    condicao = models.CharField(
        "condição", max_length=10, choices=CONDICOES, default="novo"
    )
    tags = models.CharField("tags", max_length=255, blank=True)
    estoque = models.PositiveIntegerField("estoque", default=1)
    status = models.CharField(
        "status", max_length=20, choices=STATUS, default="rascunho"
    )
    data_criacao = models.DateTimeField("data de criação", auto_now_add=True)
    data_atualizacao = models.DateTimeField("data de atualização", auto_now=True)

    class Meta:
        verbose_name = "produto"
        verbose_name_plural = "produtos"

    def __str__(self):
        return self.titulo
