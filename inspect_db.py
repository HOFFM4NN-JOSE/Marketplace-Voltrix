"""Inspeção direta do banco SQLite para verificar o superusuário admin."""

import sqlite3
from pathlib import Path

db_path = Path("db.sqlite3")
output_path = Path("inspect_db_result.txt")
with sqlite3.connect(db_path) as conn:
    cursor = conn.cursor()
    sql = (
        "SELECT id, username, email, is_superuser, is_staff, is_active "
        "FROM auth_user WHERE email = ?"
    )
    params = ("admin@voltrix.com.br",)
    cursor.execute(sql, params)
    row = cursor.fetchone()
    with open(output_path, "w", encoding="utf-8") as f:
        if row:
            f.write("|".join(str(x) for x in row))
        else:
            f.write("NOT_FOUND")
