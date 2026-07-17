from django.db import models

# CREAMOS MODELO EDITOR

class Editor(models.Model):
    nombre_editor = models.CharField(max_length = 100)
    apellido_editor = models.CharField(max_length=100)
    telefono_editor = models.CharField(max_length=50)
    email_editor = models.EmailField(max_length=50)
    website_editor = models.URLField()

class Autores(models.Model):
    nombre_autor = models.CharField(max_length = 100)
    apellido_autor = models.CharField(max_length=100)
    telefono_autor = models.CharField(max_length=100)
    email_autor = models.EmailField()
    website_autor = models.URLField()
