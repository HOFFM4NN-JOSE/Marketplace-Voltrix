"""
URL configuration for voltrix project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from . import views as voltrix_views


def home_view(request):
    """Renderiza o template `home.html` como página inicial.

    Mantemos a view simples aqui; para funcionalidade mais rica,
    considere mover para um app `core.views.HomeView`.
    """
    return render(request, "home.html")


urlpatterns = [
    path("", home_view, name="home"),
    path("loja/", voltrix_views.shop_view, name="shop"),
    path("produto/<int:pk>/", voltrix_views.product_detail_view, name="product_detail"),
    path(
        "login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"
    ),
    path("admin/", admin.site.urls),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("api/v1/", include("usuarios.urls")),
    path("api/v1/", include("produtos.urls")),
]
