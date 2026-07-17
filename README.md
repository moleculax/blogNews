##  📰 BlogNews - Plataforma de Publicación de Artículos 

## V1.0 
Plataforma  para la publicación y
gestión de artículos, desarrollada con **Django y Bootstrap**.

## 🚀 Características Principales

- 🔐 **Autenticación de usuarios** (Login/Registro)
- 📝 **CRUD completo de artículos** (Crear, Leer, Actualizar, Eliminar)
- 🏷️ **Categorías** para organizar los artículos
- 🖼️ **Gestión de imágenes** para cada artículo
- 📊 **Dashboard personalizado** para cada usuario
- ⏱️ **Tiempo de publicación** (hace X tiempo)
- 📱 **Diseño responsive** y moderno
- 🔍 **Paginación** de artículos
- 🎨 **Interfaz profesional** con Bootstrap 5

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
# o
venv\Scripts\activate  # Windows
```

## . Instalar dependencias

```
pip install -r requirements.txt
```

##  Migrar base de datos


````
python manage.py makemigrations
python manage.py migrate
````


## Ejecutar servidor

````
python manage.py runserver
```
