"""
URL configuration for blog project.
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.views import APIView

from articulosusuarios.views import PostUsuarios, UpdateArticulos, EliminarPost
from dashboard.views import DashBoard

from login.views import LogueoUsuarios, LogoutUsuarios

from registrarse.views import RegistroUsuarios

from home.views import HomePage, ArticuloDetalle

from drf_yasg.utils import swagger_auto_schema

from tools.views import FechaHora, CategoriaArticulos, PostTiempoPublicado

# Swagger Schema
schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="Descripción de tu API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@email.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# Personalización del admin
admin.site.site_header = "Administrar Gestión BLOG"
admin.site.site_title = "Panel de Control"
admin.site.index_title = "Bienvenido al Administrador"

urlpatterns = [
    # Home y Admin
    path('', HomePage.as_view(), name='home'),
    path('admin/', admin.site.urls),

    # Autenticación
    path('login/', LogueoUsuarios.as_view(), name='login'),
    path('logout/', LogoutUsuarios.as_view(), name='logout'),
    path('dashboard/', DashBoard.as_view(), name='dashboard'),

    path('accounts/login/', LoginView.as_view(), name='login'),

    path('registro/', RegistroUsuarios.as_view(), name='registro'),

    # POST USUARIOS
    path('postearArticulos', PostUsuarios.as_view(), name='post_usuarios'),
    # POST TITULO TIEMPO PUBLICADO
    path('articulo/tiempo-publicado/<int:pk>/', PostTiempoPublicado.as_view(), name='tiempo-publicado'),
    # UPDATE ARTICULOS
    path('articulo/update/<int:id>/', UpdateArticulos.as_view(), name='update_articulo'),
    # Artículos
    path('articulo/<int:id>/', ArticuloDetalle.as_view(), name='articulo_detalle'),

    # ELIMINA POST
    path('articulo/delete/<int:id>/', EliminarPost.as_view(), name='articulo_delete'),

    # ==============================================================================================

    # Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),

    path('fecha-hora/', FechaHora.as_view(), name='fecha-hora'),
    path('categorias-articulos', CategoriaArticulos.as_view(), name='categorias-articulos/'),

    # Otras URLs
    # path('hmundo/', VerHM.as_view(), name='hmundo'),
]

# ==========================================
# SIRVE ARCHIVOS MEDIA EN DESARROLLO
# ==========================================
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)