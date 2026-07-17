import datetime
import json

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from django.conf import settings
from django.db import connection


class FechaHora(APIView):
    @extend_schema(
        summary="Fecha Hora",
        description="Muestra Fecha y Hora ",
        tags=["FechaHora"],
    )
    def get_fecha_y_hora(self, request):
        fecha = datetime.datetime.now()
        formatted_fecha = fecha.strftime("%d-%m-%Y")
        formatted_hora = fecha.strftime("%H:%M")

        data = {
            'fecha': formatted_fecha,
            'hora': formatted_hora
        }

        return data


class CategoriaArticulos(APIView):

    @extend_schema(
        summary="Categoría de Artículos",
        description="Muestra la categoría de artículos",
        tags=["CategoriaArticulos"],
        responses={
            200: {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "nombre": {"type": "string"},
                        "descripcion": {"type": "string"},
                        "slug": {"type": "string"}
                    }
                }
            },
            404: {"description": "Archivo no encontrado"}
        }
    )
    def get(self, request):
        file_path = settings.BASE_DIR / 'data' / 'categorias.json'
        with open(file_path, 'r', encoding='utf-8') as file:
            categorias = json.load(file)
            return Response(categorias, status=status.HTTP_200_OK)


# HAGO CONTEO DE ARTICULOS DEL USUARIO LOGUEADO

class CountArticulosUser(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        usuario = request.user
        with connection.cursor() as cursor:
            sqlcount = """
                  SELECT COUNT(*) FROM post_articulos WHERE autor_articulo = %s
              """
            cursor.execute(sqlcount, [usuario.username])
            totalPost = cursor.fetchone()[0]

        return Response({
                     'totalPost': totalPost
                    })

class PostTiempoPublicado(APIView):
    permission_classes = [IsAuthenticated]
    # TRAIGO LOS ULTIMOS 4 POST
    def get_ultimos_articulos(self, autor):
        sql = """
            SELECT id, titular, categoria, fecha_at
                    FROM   post_articulos 
                    WHERE autor_articulo = %s  
                    AND status = 1
                    ORDER BY fecha_at DESC
                    LIMIT 4
        """
        with connection.cursor() as cursor:
            cursor.execute(sql, [autor])
            resultados = cursor.fetchall()
            articulos = []
            for fila in resultados:
                articulo = {
                    'id': fila[0],
                    'titular': fila[1],
                    'categoria': fila[2],
                    'fecha_at': fila[3]
                }
                articulos.append(articulo)
            # return Response(articulos)
            return articulos



    def get(self, request, pk):
        # Fecha y hora actual
        fecha_hora_actual = datetime.datetime.now()

        with connection.cursor() as cursor:
            sql = """
                SELECT fecha_at, titular
                FROM post_articulos WHERE id = %s
            """
            cursor.execute(sql, [pk])
            resultado = cursor.fetchone()

            # Verificar si existe el artículo
            if not resultado:
                return Response({
                    'error': 'Artículo no encontrado'
                }, status=404)

            fecha_publicacion = resultado[0]
            titular = resultado[1]

            # Calcular diferencia
            diferencia = fecha_hora_actual - fecha_publicacion

            dias = diferencia.days
            horas = diferencia.seconds // 3600
            minutos = (diferencia.seconds % 3600) // 60

            # Formatear tiempo
            if dias > 0:
                tiempo = f"{dias} día{'s' if dias > 1 else ''} atrás"
            elif horas > 0:
                tiempo = f"{horas} hora{'s' if horas > 1 else ''} atrás"
            elif minutos > 0:
                tiempo = f"{minutos} minuto{'s' if minutos > 1 else ''} atrás"
            else:
                tiempo = "Hace unos segundos"

            data = {
                'id': pk,
                'titular': titular,
                'fecha_publicacion': fecha_publicacion.strftime("%d-%m-%Y %H:%M"),
                'tiempo_publicado': tiempo
            }

            return Response(data)