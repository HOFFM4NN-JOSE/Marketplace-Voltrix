from django.shortcuts import get_object_or_404, render

from produtos.models import Produto


def shop_view(request):
    """Lista pública de produtos (vitrine) — sem login necessário."""
    produtos = Produto.objects.filter(status="ativo").order_by("-data_criacao")
    # Gera uma URL de imagem aleatória baseada no SKU para cada produto
    for p in produtos:
        p.image_url = f"https://picsum.photos/seed/{p.sku}/600/400"
    return render(request, "shop.html", {"produtos": produtos})


def product_detail_view(request, pk):
    """Detalhe público do produto."""
    produto = get_object_or_404(Produto, pk=pk, status="ativo")
    produto.image_url = f"https://picsum.photos/seed/{produto.sku}/900/600"
    return render(request, "product_detail.html", {"produto": produto})
