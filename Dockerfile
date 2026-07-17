# ============================================
# 1. IMAGEN BASE
# ============================================
FROM python:3.11-slim-bullseye

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
# 6. INSTALAR DEPENDENCIAS DE PYTHON
# ============================================
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn

# ============================================
# 7. CREAR DIRECTORIOS PARA ARCHIVOS ESTÁTICOS
# ============================================
RUN mkdir -p /app/staticfiles /app/media

# ============================================
# 8. PUERTO EXPUESTO
# ============================================
EXPOSE 8000

# ============================================
# 9. COMANDO DE INICIO
# ============================================
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "blog.wsgi:application"]