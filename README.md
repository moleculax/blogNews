# 📰 Blog News - Plataforma de Publicación de Artículos

![Django Version](https://img.shields.io/badge/Django-6.0.7-092E20?logo=django&logoColor=white)
![Python Version](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?logo=docker&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?logo=bootstrap&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Development-003B57?logo=sqlite&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Compatible-4169E1?logo=postgresql&logoColor=white)
![MariaDB](https://img.shields.io/badge/MariaDB-Compatible-003545?logo=mariadb&logoColor=white)
![REST API](https://img.shields.io/badge/REST-API-FF6C37?logo=postman&logoColor=white)
![Swagger](https://img.shields.io/badge/Swagger-Documentation-85EA2D?logo=swagger&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-Authentication-000000?logo=jsonwebtokens&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?logo=github&logoColor=white)

Plataforma moderna y profesional para la publicación y gestión de artículos, construida con Django y Bootstrap.

## 🚀 Características Principales

- 🔐 **Autenticación de usuarios** (Login/Registro) con JWT
- 📝 **CRUD completo de artículos** (Crear, Leer, Actualizar, Eliminar)
- 🏷️ **Categorías** para organizar los artículos
- 🖼️ **Gestión de imágenes** para cada artículo
- 📊 **Dashboard personalizado** para cada usuario
- ⏱️ **Tiempo de publicación** (hace X tiempo)
- 📱 **Diseño responsive** y moderno con Bootstrap 5
- 🔍 **Paginación** de artículos
- 🎨 **Interfaz profesional** con Bootstrap Icons
- 🐳 **Despliegue con Docker**

## 🛠️ Tecnologías Utilizadas

| Tecnología | Descripción | Badge |
|------------|-------------|-------|
| **Backend** | Django 6.0.7 | ![Django](https://img.shields.io/badge/Django-6.0.7-092E20?logo=django&logoColor=white) |
| **Frontend** | Bootstrap 5, Bootstrap Icons | ![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?logo=bootstrap&logoColor=white) |
| **Base de Datos** | SQLite (desarrollo) / PostgreSQL / MariaDB | ![SQLite](https://img.shields.io/badge/SQLite-Dev-003B57?logo=sqlite&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-OK-4169E1?logo=postgresql&logoColor=white) |
| **Autenticación** | Django Auth con modelo personalizado + JWT | ![JWT](https://img.shields.io/badge/JWT-Auth-000000?logo=jsonwebtokens&logoColor=white) |
| **API** | Django REST Framework | ![REST API](https://img.shields.io/badge/REST-API-FF6C37?logo=postman&logoColor=white) |
| **Documentación API** | drf-yasg (Swagger) | ![Swagger](https://img.shields.io/badge/Swagger-Docs-85EA2D?logo=swagger&logoColor=white) |
| **Alertas** | SweetAlert2 | ![SweetAlert2](https://img.shields.io/badge/SweetAlert2-Alerts-FF6C37) |
| **Docker** | Containerización | ![Docker](https://img.shields.io/badge/Docker-Container-2496ED?logo=docker&logoColor=white) |



[![Blog News Screenshot](https://raw.githubusercontent.com/moleculax/blogNews/main/media/imagenarticulos/blogNew_00.png)](https://github.com/moleculax/blogNews/blob/main/media/imagenarticulos/blogNew_00.png)



## 🐳  PRUEBELO USANDO DOCKER

**Construir directamente desde GitHub (sin clonar)**

```
sudo docker build -t blog-news:latest https://github.com/moleculax/blogNews.git#main
```
## Verificar que la imagen se creó
```
# Listar las imágenes Docker
docker images
```
## Ejecutar en modo simple
```
docker run -p 8000:8000 blog-news:latest
```
##  Verificar que funciona
```
# Ver logs en tiempo real
docker logs -f blog-container

# Ver logs de los últimos 50 líneas
docker logs --tail 50 blog-container
```
##  Acceder a la aplicación
```
http://localhost:8000

http://localhost:8000/swagger/
```

## Lo que va a pasar
Docker descargará el código desde GitHub

Instalará las dependencias del sistema (git, gcc)

Clonará tu repositorio dentro del contenedor

Instalará las dependencias de Python desde requirements.txt

Instalará Gunicorn (servidor web)

Creará la imagen lista para ejecutar


## OJO:
🐳 Reconstruir la imagen
```
# Limpiar caché de Docker
sudo docker system prune -f

# Reconstruir la imagen
sudo docker build -t blog-news:latest https://github.com/moleculax/blogNews.git#main

# Ejecutar el contenedor
sudo docker run -p 8000:8000 blog-news:latest
```
**Probado en Debian 13, tambien puede ejecutarse sin problemas en Windows**

![Blog News Screenshot](https://raw.githubusercontent.com/moleculax/blogNews/main/media/imagenarticulos/blognews_0.png)


**🚀 TODO EL PROYECTO ESTÁ COMPLETO. y se ajustara periodicamente**