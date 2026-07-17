##  📰 BlogNews - Plataforma de Publicación de Artículos 

## V1.0 
Plataforma  para la publicación y
gestión de artículos, desarrollada con **Django y Bootstrap**.

[![Blog News Screenshot](https://raw.githubusercontent.com/moleculax/blogNews/main/media/imagenarticulos/blogNew_00.png)](https://github.com/moleculax/blogNews/blob/main/media/imagenarticulos/blogNew_00.png)

## 🚀 Características Principales

- 🔐 **Autenticación de usuarios** (Login/Registro)
- 📝 **CRUD completo de artículos** (Crear, Leer, Actualizar, Eliminar)
- 🏷️ **Categorías** para organizar los artículos
- 🖼️ **Gestión de imágenes** para cada artículo
- 📊 **Dashboard personalizado** para cada usuario
- ⏱️ **Tiempo de publicación** (hace X tiempo)
- 📱 **Diseño responsive**
- 🔍 **Paginación** de artículos
- 🎨 **Interfaz** con Bootstrap 5


![Blog News Screenshot](https://raw.githubusercontent.com/moleculax/blogNews/main/media/imagenarticulos/blognews_0.png)

## 🛠️ Tecnologías Utilizadas

- **Backend**: Django 6.0.7
- **Frontend**: Bootstrap 5, Bootstrap Icons
- **Base de Datos**: SQLite (desarrollo) Puede migrar a postgreSQL/MariaDB
- **Autenticación**: Django Auth con modelo personalizado
- **API**: Django REST Framework
- **Documentación API**: drf-yasg (Swagger)
- **Librerías adicionales**: 
  - SweetAlert2 para alertas
  - djangorestframework-simplejwt para JWT
- **Docker**

## Crear y activar entorno virtual
 ```
python -m venv venv
source venv/bin/activate  # Linux/Mac

```

## . Instalar dependencias

```
pip install -r requirements.txt
```

##  Migrar base de datos

````
python3 manage.py makemigrations
python3 manage.py migrate
````
## Create superuser
```
python3 manage.py createsuperuser
```

## Ejecutar servidor

```
python3 manage.py runserver
```

## SI QUIERES USAR DOCKER

**Construir directamente desde GitHub (sin clonar)**

```
docker build -t blog-news:latest https://github.com/moleculax/blogNews.git#main
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

**🚀 TODO EL PROYECTO ESTÁ COMPLETO. y se ajustara periodicamente**