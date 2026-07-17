#!/bin/bash
# entrypoint.sh - Script de inicio con detección de SQLite

set -e

echo "=========================================="
echo "🚀 Iniciando Blog News..."
echo "=========================================="

# ============================================
# 1. CREAR DIRECTORIOS NECESARIOS
# ============================================
echo "📁 Creando directorios..."
mkdir -p /app/staticfiles /app/media /app/data /app/logs

# ============================================
# 2. DETECTAR SI EXISTE LA BASE DE DATOS
# ============================================
DB_PATH="/app/db.sqlite3"

if [ -f "$DB_PATH" ]; then
    echo "✅ Base de datos SQLite encontrada en: $DB_PATH"
    echo "📊 Tamaño: $(du -h $DB_PATH | cut -f1)"
    echo "ℹ️  No se crearán migraciones nuevas"
else
    echo "❌ Base de datos SQLite NO encontrada en: $DB_PATH"
    echo "🔄 Creando nueva base de datos..."
    echo "🔄 Ejecutando migraciones por primera vez..."
    python manage.py migrate --noinput
    echo "✅ Base de datos creada exitosamente"
fi

# ============================================
# 3. RECOPILAR ARCHIVOS ESTÁTICOS (siempre)
# ============================================
echo "📦 Recopilando archivos estáticos..."
python manage.py collectstatic --noinput

# ============================================
# 4. CREAR SUPERUSUARIO (solo si no existe)
# ============================================
echo "🔧 Verificando superusuario..."
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(is_superuser=True).exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('✅ Superusuario creado: admin / admin123')
else:
    print(' Superusuario ya existe')
"

# ============================================
# 5. VERIFICAR CATEGORÍAS (cargar si no existen)
# ============================================
echo " Verificando categorías..."
python manage.py shell -c "
import json
from django.conf import settings
from django.db import connection

# Verificar si la tabla categorias existe
with connection.cursor() as cursor:
    cursor.execute(\"SELECT name FROM sqlite_master WHERE type='table' AND name='categorias'\")
    if cursor.fetchone():
        cursor.execute(\"SELECT COUNT(*) FROM categorias\")
        count = cursor.fetchone()[0]
        if count == 0:
            print('📂 Cargando categorías...')
            try:
                with open('/app/data/categorias.json', 'r', encoding='utf-8') as f:
                    categorias = json.load(f)
                    for cat in categorias:
                        cursor.execute(
                            \"INSERT INTO categorias (id, nombre, descripcion, slug) VALUES (%s, %s, %s, %s)\",
                            [cat['id'], cat['nombre'], cat['descripcion'], cat['slug']]
                        )
                    print(f'✅ {len(categorias)} categorías cargadas')
            except FileNotFoundError:
                print('⚠️  Archivo categorias.json no encontrado')
        else:
            print(f'ℹ️  {count} categorías ya existen')
    else:
        print('ℹ️  Tabla categorias no existe aún')
"

# ============================================
# 6. MOSTRAR INFORMACIÓN
# ============================================
echo "=========================================="
echo "✅ Blog News listo para ejecutarse"
echo "📍 Base de datos: $DB_PATH"
echo "📊 Tamaño: $(du -h $DB_PATH 2>/dev/null | cut -f1 || echo '0B')"
echo "🌐 Servidor: http://0.0.0.0:8000"
echo "📚 Swagger: http://0.0.0.0:8000/swagger/"
echo "🔧 Admin: http://0.0.0.0:8000/admin/"
echo "=========================================="

# ============================================
# 7. INICIAR GUNICORN
# ============================================
echo " Iniciando Gunicorn..."
exec gunicorn --bind 0.0.0.0:8000 \
    --workers 3 \
    --threads 2 \
    --worker-class sync \
    --timeout 120 \
    --access-logfile /app/logs/gunicorn-access.log \
    --error-logfile /app/logs/gunicorn-error.log \
    blog.wsgi:application