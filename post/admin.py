# post/admin.py
from django.contrib import admin



from .models import Articulos, Comentarios, Categorias


class ArticulosAdmin(admin.ModelAdmin):
    list_display = ('titular', 'autor_articulo', 'fecha_at', 'status')
    list_filter = ('status', 'fecha_at')
    search_fields = ('titular', 'autor_articulo', 'articulo')
    ordering = ('-fecha_at',)
    list_editable = ('status',)
    readonly_fields = ('fecha_at', 'fecha_up')


class ComentariosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'comentario', 'fecha_at', 'activo')
    list_filter = ('activo', 'fecha_at')
    search_fields = ('nombre', 'comentario')
    ordering = ('-fecha_at',)
    list_editable = ('activo',)

class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('tipocategoria',)

# Registrar los modelos con sus configuraciones
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Comentarios, ComentariosAdmin)
admin.site.register(Categorias, CategoriasAdmin)