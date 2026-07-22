"""Gera 2 produtos de exemplo para cada usuário com perfil 'vendedor'."""

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "voltrix.settings")
import django  # noqa: E402

django.setup()
import random  # noqa: E402

from django.contrib.auth import get_user_model  # noqa: E402
from django.utils.text import slugify  # noqa: E402

from produtos.models import Categoria, Marca, Produto  # noqa: E402

User = get_user_model()

categoria, _ = Categoria.objects.get_or_create(
    nome="Peças de Computador",
    defaults={
        "slug": "pecas-de-computador",
        "descricao": "Componentes e periféricos para computadores.",
    },
)
marca, _ = Marca.objects.get_or_create(nome="Genérico", defaults={"slug": "generico"})

vendedores = User.objects.filter(perfil="vendedor")

amostras = [
    ("Placa de Vídeo GTX 1660 Super", "Placa de vídeo usada, excelente estado."),
    ("Memória DDR4 8GB 2666MHz", "Memória de alto desempenho para jogos."),
    ("Fonte 600W 80 Plus Bronze", "Fonte confiável com cabo modular."),
    ("SSD NVMe 500GB", "Disco rápido para sistema operacional."),
    ("Cooler para CPU RGB", "Refrigeração eficiente com iluminação RGB."),
    ("Processador Ryzen 5 3600", "Ótimo custo-benefício para produtividade e jogos."),
]

created = []
for vendedor in vendedores:
    for i in range(2):
        sample = random.choice(amostras)
        titulo = f"{sample[0]} - {vendedor.username} #{i+1}"
        descricao_curta = sample[1]
        descricao_completa = (
            f"{sample[1]}\n"
            "Vendido por "
            f"{vendedor.username} "
            "na Voltrix. Produto de exemplo gerado automaticamente."
        )
        sku = f"{vendedor.username.upper()}-{i+1}-{random.randint(1000, 9999)}"
        slug = slugify(titulo)
        preco = round(random.uniform(50, 1500), 2)
        produto, created_flag = Produto.objects.get_or_create(
            sku=sku,
            defaults={
                "vendedor": vendedor,
                "categoria": categoria,
                "marca": marca,
                "titulo": titulo,
                "slug": slug,
                "descricao_curta": descricao_curta,
                "descricao_completa": descricao_completa,
                "preco": preco,
                "quantidade": random.randint(1, 10),
                "estoque": random.randint(1, 10),
                "status": "ativo",
            },
        )
        created.append((produto.sku, created_flag, produto.titulo))

print("PRODUTOS_CREATED_OR_FOUND:")
for c in created:
    print(c)
print("TOTAL_PRODUTOS:", Produto.objects.filter(status="ativo").count())
