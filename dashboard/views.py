from django.shortcuts import render
from django.views import View

from tools.views import CountArticulosUser, PostTiempoPublicado


class DashBoard(View):
    def get(self, request):
        totalArticulos = CountArticulosUser()
        response = totalArticulos.get(request)
        conteo = response.data if response.status_code == 200 else {'totalPost': 0}

        # Últimos artículos del usuario
        ultimosPost = PostTiempoPublicado()
        misPost = ultimosPost.get_ultimos_articulos(request.user.username)

        # OBTENGO DETALLES
        datosUltimosPost = []
        for articulo in misPost:  # articuloES UN DICCIONARIO
            elId = articulo['id']
            # Llamar al método get y obtener los datos
            responsedatos = ultimosPost.get(request, pk=elId)
            if responsedatos.status_code == 200:
                fecha_publicacion = responsedatos.data['fecha_publicacion']
                tiempo_publicado = responsedatos.data['tiempo_publicado']

                # Guardar ambos datos juntos
                datosUltimosPost.append({
                    'id': elId,
                    'titular': articulo['titular'],
                    'categoria': articulo['categoria'],
                    'fecha_publicacion': fecha_publicacion,
                    'tiempo_publicado': tiempo_publicado
                })


        datos = {
            'conteo': conteo,
            'datosUltimosPost': datosUltimosPost
        }

        print('datos',datos)

        return render(request, 'dashboard/dashboard.html', datos)