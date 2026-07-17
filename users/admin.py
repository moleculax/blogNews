from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models  import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
	pass
	# Añadimos los campos custom a la vista de admin
	fieldsets = (
		(None, {'fields': ('username', 'password')}),
		('Información personal', {'fields': ('first_name', 'last_name', 'email', 'bio', 'avatar')}),
		('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
		('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
	)
	readonly_fields = ('last_login', 'date_joined')

