"""Inspeciona o superusuário admin e grava resultados em arquivo."""

import os

import django  # noqa: E402

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "voltrix.settings")
django.setup()
from django.contrib.auth import get_user_model  # noqa: E402

User = get_user_model()

results = []
qs = User.objects.filter(email="admin@voltrix.com.br")
results.append(f"count={qs.count()}")
if qs.exists():
    u = qs.first()
    results.append(f"pk={u.pk}")
    results.append(f"email={u.email}")
    results.append(f"username={u.username}")
    results.append(f"is_superuser={u.is_superuser}")
    results.append(f"is_staff={u.is_staff}")
    results.append(f"is_active={u.is_active}")
    results.append(f"has_usable_password={u.has_usable_password()}")
    results.append(f'check_password={u.check_password("Raioroxo101@")}')

with open("inspect_admin_result.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(results))
