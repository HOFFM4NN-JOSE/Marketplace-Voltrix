# Voltrix Marketplace

## Visão geral

O Voltrix é um marketplace profissional, criado do zero com Django, Django REST Framework, PostgreSQL, Redis, Celery, Docker e documentação OpenAPI. O projeto foi estruturado com foco em escalabilidade, segurança, organização modular e boas práticas de engenharia.

## Arquitetura inicial

- Backend: Django 5.2.1
- API: Django REST Framework
- Banco de dados: SQLite para desenvolvimento, PostgreSQL para produção
- Filas: Celery + Redis
- Documentação: drf-spectacular
- Organização: apps separados por responsabilidade

## Apps implementados

- usuarios: autenticação, perfis e usuários
- produtos: categorias, marcas e anúncios

## Como executar

1. Crie e ative o ambiente virtual.
2. Instale as dependências com pip.
3. Execute as migrações.
4. Inicie o servidor de desenvolvimento.

```bash
python manage.py migrate
python manage.py runserver
```

## Próximas etapas

- implementar pedidos e carrinho
- implementar mensagens e WhatsApp
- implementar painel administrativo
- preparar Docker e deploy
