"""Script para instalar dependências do projeto Voltrix e registrar o resultado."""

import subprocess
import sys
from pathlib import Path

log_path = Path("install_dependencies_log.txt")
requirements = Path("requirements.txt")


def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr


with log_path.open("w", encoding="utf-8") as log_file:
    log_file.write(f"Python: {sys.executable}\n")
    if requirements.exists():
        command = [sys.executable, "-m", "pip", "install", "-r", str(requirements)]
        returncode, stdout, stderr = run_command(command)
        log_file.write("PIP INSTALL RETURN CODE: " + str(returncode) + "\n")
        log_file.write("STDOUT:\n" + stdout + "\n")
        log_file.write("STDERR:\n" + stderr + "\n")
    else:
        log_file.write("requirements.txt não encontrado\n")

    command = [sys.executable, "-m", "pip", "list", "--format=freeze"]
    returncode, stdout, stderr = run_command(command)
    log_file.write("PIP LIST RETURN CODE: " + str(returncode) + "\n")
    log_file.write("PACKAGES:\n" + stdout + "\n")
    log_file.write("PIP LIST STDERR:\n" + stderr + "\n")

    packages = [
        "django",
        "djangorestframework",
        "psycopg",
        "celery",
        "redis",
        "gunicorn",
        "Pillow",
        "django-environ",
        "whitenoise",
        "drf-spectacular",
        "pytest-django",
    ]
    log_file.write("PACKAGE IMPORT CHECKS:\n")
    for package in packages:
        try:
            mod = __import__(package)
            log_file.write(f'{package}: OK {getattr(mod, "__version__", "unknown")}\n')
        except Exception as e:
            log_file.write(f"{package}: ERR {e}\n")
