from enum import unique

from django.db import models
from django.contrib.auth.models import AbstractUser


# Modelo de usuario personalizado extendiendo AbstractUser.
# Añade algunos campos opcionales (bio, avatar, is_verified).
class User(AbstractUser):
    email = models.EmailField(unique=True)

    # AGREGADO PARA LOGUEAR CON EMAIL
    # LA CREACION DEL SUPERUSER TIENE QUE SER ANTE DE MODIFICAR O AGREGAR ESTO
    # PARA CREAR OTRO SUPERUSER BASTA CON COMENTAR ESTAS DOS LINEAS Y LUEGO ACTIVARLAS
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    # ================================================================================

    bio = models.TextField('Biografía', blank=True, null=True)
    avatar = models.ImageField('Avatar', upload_to='avatars/', blank=True, null=True)
    is_verified = models.BooleanField('Verificado', default=False)

    def __str__(self) -> str:
        return f"{self.username} ({self.email})"