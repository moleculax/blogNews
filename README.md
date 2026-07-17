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
