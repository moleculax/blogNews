import datetime

from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.db import connection
from django.http import HttpResponse, Http404
# home/views.py
from django.shortcuts import render
from django.views import View
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView

from tools.views import FechaHora, CategoriaArticulos


# AQUI CREO EL HOME PAGE

class HomePageTest(View):
    def get(self, request):
        return render(request, 'home/home.html')


# class HomePageArticulos(View):
#     def get(self, request):
#         # Instancia las vistas
#         home_page = HomePage()
#         ver_hm = VerHM()
#
#         # Obtén los datos de cada vista
#         # Nota: VerHM.get() espera un request
#         datos_home = home_page.get(request)  # Esto devuelve un HttpResponse
#         datos_ver_hm = ver_hm.get(request)  # Esto devuelve un HttpResponse
#
#         # Usa los datos como necesites
#         # Por ejemplo, combina la información o redirige
#         return datos_home  # O return datos_ver_hm


# MUESTRA RESULTADOS CON PAGINADOR EN EL HOMEPAGE
class HomePage(View):
    def get(self, request):

    # INTANCIO CLASS CON FECHA/HORA
        fecha_hora = FechaHora()
    # Llamo al metodo get_fecha_y_hora
    # OJO puedo sustituir reques por none en get_fecha_y_hora porque no lo necesito
        datos = fecha_hora.get_fecha_y_hora(request)
    # Extraigo  los valores
        fecha = datos['fecha']
        hora = datos['hora']

    # ================================
        page = request.GET.get('page', 1)

        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM post_articulos WHERE status = true")
            total = cursor.fetchone()[0]

            limit = 8
            offset = (int(page) - 1) * limit

            cursor.execute("""
                SELECT id,
                titular,
                articulo,
                autor_articulo,
                fecha_at,
                imagen_articulo,
                categoria
                FROM post_articulos
                WHERE status = true
                ORDER BY fecha_at DESC
                LIMIT %s OFFSET %s
            """, [limit, offset])

            columnas = [col[0] for col in cursor.description]
            articulos = []
            for fila in cursor.fetchall():
                articulo = dict(zip(columnas, fila))
                articulos.append(articulo)

        paginator = Paginator(articulos, limit)

        try:
            articulos_paginados = paginator.page(page)
        except PageNotAnInteger:
            articulos_paginados = paginator.page(1)
        except EmptyPage:
            articulos_paginados = paginator.page(paginator.num_pages)


        return render(request, 'home/home.html', {
            'articulos': articulos_paginados,
            'total_articulos': total,
            'fechaServer': fecha,
            'horaServer': hora,

        })


class VerHM(APIView):

    @extend_schema(
        summary="HMundo cruel",
        description="Esta es una prueba de funcionamiento",
        tags=["Hmundo"],
    )

    def get_fecha_y_hora(request):
        fecha = datetime.now()
        formatted_fecha = fecha.strftime("%d-%m-%Y")
        formatted_hora = fecha.strftime("%H:%M")

        return {"fecha": formatted_fecha, "hora": formatted_hora}

    def get(self, request):
        fecha_hora = datetime.datetime.now()
        hora = fecha_hora.strftime("%H:%M")
        fecha = fecha_hora.strftime("%d-%m-%Y")
        fn = "Fecha: "+fecha+" Hora: "+hora
        html = """
                    <html>
                    <body>
                    <h1>Hola Mundo Cruel...</h1>
                    <h3>%s<h/3>
                    </body>
                    </html> 
                 """
        return HttpResponse(html % fn)




# ==========================================
# VISTA PARA ARTÍCULO COMPLETO
# ==========================================
class ArticuloDetalle(View):
    def get(self, request, id):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id, 
                titular, 
                articulo, 
                autor_articulo, 
                fecha_at,
                imagen_articulo,
                categoria
                FROM post_articulos
                WHERE id = %s AND status = true
            """, [id])

            fila = cursor.fetchone()

            if not fila:
                raise Http404("Artículo no encontrado")

            columnas = [col[0] for col in cursor.description]
            articulo = dict(zip(columnas, fila))

        return render(request, 'articulos/articulo_detalle.html', {'articulo': articulo})



