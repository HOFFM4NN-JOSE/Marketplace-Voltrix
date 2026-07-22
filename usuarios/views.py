"""Views do módulo de usuários do Voltrix."""

from rest_framework import generics

from .models import Usuario
from .serializers import UsuarioSerializer


class UsuarioListView(generics.ListAPIView):
    """Lista usuários ativos para fins de administração e consulta."""

    queryset = Usuario.objects.filter(esta_ativo=True)
    serializer_class = UsuarioSerializer
