# articulosusuarios/views.py
from django.db import connection
from django.http import request
from django.shortcuts import render, redirect
from rest_framework.views import APIView, View
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_spectacular.utils import extend_schema
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import os
import base64
from datetime import datetime

from tools.views import CategoriaArticulos


class PostUsuarios(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Obtener categorías de los articulos
        categorias_articulos = CategoriaArticulos()
        response = categorias_articulos.get(request)
        categorias = response.data
        # ==========================================
        return render(request, 'articulosusuarios/post_articulo.html', {'categorias': categorias})

    def post(self, request):
        usuario = request.user
        content_type = request.content_type

        if 'multipart/form-data' in content_type:
            titular = request.POST.get('titular')
            articulo = request.POST.get('articulo')
            status = request.POST.get('status', 'True')
            imagen = request.FILES.get('imagen_articulo')
            categoria = request.POST.get('categoria')

            # Procesar la imagen
            imagen_path = ''
            if imagen:
                # Crear nombre único para la imagen
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                nombre_archivo = f"imagenarticulos/{timestamp}_{imagen.name}"

                # Guardar la imagen en MEDIA_ROOT/imagenarticulos/
                path = default_storage.save(nombre_archivo, ContentFile(imagen.read()))
                imagen_path = path  # Esto guarda 'imagenarticulos/nombre_archivo.jpg'

            # Guardar en la base de datos
            sql = """
                INSERT INTO post_articulos (
                    titular,
                    articulo, 
                    autor_articulo, 
                    fecha_at, 
                    fecha_up, 
                    status, 
                    imagen_articulo,
                    categoria
                ) VALUES (
                    %s,
                    %s,
                    %s,
                    datetime('now'), 
                    datetime('now'),
                    %s,
                    %s,
                    %s
                )
            """

            with connection.cursor() as cursor:
                cursor.execute(sql, [titular, articulo, usuario.username, status == 'True', imagen_path,categoria])
            #
            # return Response({
            #     'message': 'exito',
            #     'usuario': usuario.username,
            #     'data': {
            #         'titular': titular,
            #         'articulo': articulo,
            #         'status': status,
            #         'imagen_articulo': imagen_path
            #     }
            # }, status=201)
                # ===== REDIRIGE AL DASHBOARD =====
                return redirect('dashboard')
                # ==================================

        else:
            return Response({'error': 'Tipo de contenido no soportado'}, status=400)


class UpdateArticulos(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):

        # INSTANCIO CLASS QUE TIENE EL JSON PARA USARLO EN LA VISTA
        datosjsoncategorias = CategoriaArticulos()
        categoriasjson = datosjsoncategorias.get(request)
        # ==========================================================
        try:



            with connection.cursor() as cursor:
                sql = """
                        SELECT id, titular,
                        articulo, status,
                        imagen_articulo,
                        categoria
                        FROM post_articulos
                        WHERE id = %s AND autor_articulo = %s
                     """
                cursor.execute(sql, [id, request.user.username])

                fila = cursor.fetchone()

                if not fila:
                    return render(request, 'articulosusuarios/update_articulo.html', {
                        'error': 'Artículo no encontrado o no tienes permiso para editarlo'
                    })

                articulo = {
                    'id': fila[0],
                    'titular': fila[1],
                    'articulo': fila[2],
                    'status': fila[3],
                    'imagen_articulo': fila[4],
                    'categoria': fila[5]
                }
                print('categoriasjson: ', categoriasjson.data)
                return render(request, 'articulosusuarios/update_articulo.html', {
                    'articulo': articulo,
                    'categoriasjson': categoriasjson.data
                })

        except Exception as e:
            return render(request, 'articulosusuarios/update_articulo.html', {
                'error': f'Error al obtener el artículo: {str(e)}'
            })

    def post(self, request, id):
        usuario = request.user
        content_type = request.content_type

        if 'multipart/form-data' in content_type:
            titular = request.POST.get('titular')
            articulo = request.POST.get('articulo')
            status = request.POST.get('status', 'True')
            categoria = request.POST.get('categoria')  # <--- Cambiado a categoria
            imagen = request.FILES.get('imagen_articulo')

            # Verificar que el artículo existe y pertenece al usuario
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT autor_articulo FROM post_articulos WHERE id = %s
                """, [id])
                fila = cursor.fetchone()

                if not fila:
                    return Response({'error': 'Artículo no encontrado'}, status=404)

                if fila[0] != usuario.username:
                    return Response({'error': 'No tienes permiso para editar este artículo'}, status=403)

            # Procesar la imagen si se sube una nueva
            imagen_path = None
            if imagen:
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                nombre_archivo = f"imagenarticulos/{timestamp}_{imagen.name}"
                path = default_storage.save(nombre_archivo, ContentFile(imagen.read()))
                imagen_path = path

            # Actualizar en la base de datos
            if imagen_path:
                sql = """
                    UPDATE post_articulos 
                    SET titular = %s,
                        articulo = %s,
                        fecha_up = datetime('now'),
                        status = %s,
                        imagen_articulo = %s,
                        categoria = %s
                    WHERE id = %s AND autor_articulo = %s
                """
                params = [titular, articulo, status == 'True', imagen_path, categoria, id, usuario.username]
            else:
                sql = """
                    UPDATE post_articulos 
                    SET titular = %s,
                        articulo = %s,
                        fecha_up = datetime('now'),
                        status = %s,
                        categoria = %s
                    WHERE id = %s AND autor_articulo = %s
                """
                params = [titular, articulo, status == 'True', categoria, id, usuario.username]

            with connection.cursor() as cursor:
                cursor.execute(sql, params)

            return redirect('dashboard')

        else:
            return Response({'error': 'Tipo de contenido no soportado'}, status=400)


from django.contrib import messages


class EliminarPost(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        sql_select = """SELECT id FROM post_articulos WHERE id = %s"""
        sql_delete = """DELETE FROM post_articulos WHERE id = %s"""

        with connection.cursor() as cursor:
            cursor.execute(sql_select, [id])
            resultado = cursor.fetchone()

            if not resultado:
                messages.error(request, 'Artículo no encontrado')
                return redirect('dashboard')

            cursor.execute(sql_delete, [id])
            messages.success(request, 'Artículo eliminado correctamente')

        return redirect('dashboard')