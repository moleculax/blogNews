# post/models.py
from django.db import models


# CREAMOS EL MODELO PARA POST DE ARTICULOS
class Articulos(models.Model):
    titular = models.CharField(max_length=200)
    articulo = models.TextField()
    autor_articulo = models.CharField(max_length=100)
    fecha_at = models.DateTimeField(auto_now_add=True)
    fecha_up = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    categoria = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    imagen_articulo = models.ImageField('imagenarticulos', upload_to='imagenarticulos/', blank=True, null=True)


class Categorias(models.Model):
    tipocategoria = models.CharField(max_length=100)


# CREAMOS EL MODELO DE COMENTARIOS DE ARTICULOS
class Comentarios(models.Model):
    comentario = models.TextField()
    nombre = models.CharField(max_length=100)
    fecha_at = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)





