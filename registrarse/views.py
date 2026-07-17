from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User

class RegistroUsuarios(APIView):

    def get(self,request):
        return render(request, 'registro/registrarse.html')

    def post(self, request):
        # optenemos los datos del request
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')

        # Validamos los datos
        if not username or not email or not password:
            return Response({'error': 'Todos los campos son requeridos.'}, status=400)
        # Chequeamos si el usuario o email existen
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username existe o esta registrado.'}, status=400)

        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email existe o esta registrado.'}, status=400)
        # Creamos el usuario
        user = User.objects.create_user(
                                        username=username,
                                        email=email,
                                        password=password,
                                        first_name = first_name,
                                        last_name = last_name,
                                        is_active=True,
                                        is_staff=False
                                        )

        # return Response({'message': 'User registered successfully.'}, status=201)
        return render(request, 'login/login.html', status=200)
