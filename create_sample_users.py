"""Cria usuários de teste: 5 clientes e 5 vendedores."""

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "voltrix.settings")
import django  # noqa: E402

django.setup()
from django.contrib.auth import get_user_model  # noqa: E402

User = get_user_model()

clientes = [
    ("cliente1@voltrix.com.br", "cliente1", "Cliente Um"),
    ("cliente2@voltrix.com.br", "cliente2", "Cliente Dois"),
    ("cliente3@voltrix.com.br", "cliente3", "Cliente Três"),
    ("cliente4@voltrix.com.br", "cliente4", "Cliente Quatro"),
    ("cliente5@voltrix.com.br", "cliente5", "Cliente Cinco"),
]

vendedores = [
    ("vendedor1@voltrix.com.br", "vendedor1", "Vendedor Um"),
    ("vendedor2@voltrix.com.br", "vendedor2", "Vendedor Dois"),
    ("vendedor3@voltrix.com.br", "vendedor3", "Vendedor Três"),
    ("vendedor4@voltrix.com.br", "vendedor4", "Vendedor Quatro"),
    ("vendedor5@voltrix.com.br", "vendedor5", "Vendedor Cinco"),
]

PASSWORD = "SenhaPadrao123!"

created = []
for email, username, nome in clientes:
    u, c = User.objects.get_or_create(
        email=email,
        defaults={
            "username": username,
            "nome_completo": nome,
            "perfil": "cliente",
            "is_active": True,
        },
    )
    if c or not u.check_password(PASSWORD):
        u.set_password(PASSWORD)
        u.save()
    created.append((email, u.perfil))

for email, username, nome in vendedores:
    u, c = User.objects.get_or_create(
        email=email,
        defaults={
            "username": username,
            "nome_completo": nome,
            "perfil": "vendedor",
            "is_active": True,
        },
    )
    if c or not u.check_password(PASSWORD):
        u.set_password(PASSWORD)
        u.save()
    created.append((email, u.perfil))

print("USERS_CREATED_OR_UPDATED:", created)
print("PASSWORD_FOR_ALL:", PASSWORD)
print("TOTAL_USERS_IN_DB:", User.objects.count())
