# ============================================
# 1. IMAGEN BASE
# ============================================
FROM python:3.12-slim

# ============================================
# 2. VARIABLES DE ENTORNO
# ============================================
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=blog.settings

# ============================================
# 3. INSTALAR DEPENDENCIAS DEL SISTEMA
# ============================================
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    git \
    && rm -rf /var/lib/apt/lists/*

# ============================================
# 4. CLONAR EL REPOSITORIO DESDE GITHUB
# ============================================
RUN git clone --depth 1 --branch main https://github.com/moleculax/blogNews.git /app

# ============================================
# 5. DIRECTORIO DE TRABAJO
# ============================================
WORKDIR /app

# ============================================
# 6. ACTUALIZAR PIP
# ============================================
RUN pip install --upgrade pip

# ============================================
# 7. INSTALAR DEPENDENCIAS
# ============================================
RUN pip install --no-cache-dir -r requirements.txt

# ============================================
# 8. CREAR DIRECTORIOS
# ============================================
RUN mkdir -p /app/staticfiles /app/media /app/data

# ============================================
# 9. PUERTO EXPUESTO
# ============================================
EXPOSE 8000

# ============================================
# 10. COMANDO DE INICIO
# ============================================
CMD ["sh", "-c", "python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn --bind 0.0.0.0:8000 blog.wsgi:application"]