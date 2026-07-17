from django.contrib import admin
from .models import Editor, Autores


class EditorAdmin(admin.ModelAdmin):
    list_display = ('nombre_editor', 'apellido_editor', 'telefono_editor', 'email_editor', 'website_editor')
    search_fields = ('nombre_editor', 'apellido_editor', 'email_editor')

class AutoresAdmin(admin.ModelAdmin):
    list_display = ('nombre_autor', 'apellido_autor', 'telefono_autor', 'email_autor', 'website_autor')
    search_fields = ('nombre_autor', 'apellido_autor', 'email_autor')

# Register your models here.
admin.site.register(Editor, EditorAdmin)
admin.site.register(Autores, AutoresAdmin)

