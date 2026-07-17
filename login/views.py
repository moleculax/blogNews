from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class LogueoUsuarios(APIView):

    @swagger_auto_schema(
        operation_description="Página de login",
        responses={200: 'Página de login'}
    )
    def get(self, request):
        return render(request, 'login/login.html')

    @swagger_auto_schema(
        operation_description="Login de usuario",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='Email del usuario',
                    example='usuario@ejemplo.com'  # Email de ejemplo genérico
                ),
                'password': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='Contraseña del usuario',
                    example='contraseña123'  
                ),
            },
            required=['email', 'password']
        ),
        responses={
            200: openapi.Response(
                description='Login exitoso con token',
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'success': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                        'message': openapi.Schema(type=openapi.TYPE_STRING),
                        'access': openapi.Schema(type=openapi.TYPE_STRING, description='Token de acceso'),
                        'refresh': openapi.Schema(type=openapi.TYPE_STRING, description='Token de refresco'),
                        'redirect': openapi.Schema(type=openapi.TYPE_STRING),
                    }
                )
            ),
            400: openapi.Response(
                description='Credenciales inválidas',
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'success': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                        'error': openapi.Schema(type=openapi.TYPE_STRING),
                    }
                )
            )
        }
    )
    def post(self, request):
        # Intentar obtener datos de JSON o de formulario
        if request.content_type == 'application/json':
            email = request.data.get('email')
            password = request.data.get('password')
        else:
            email = request.POST.get('email')
            password = request.POST.get('password')

        # Verificar que los campos no estén vacíos
        if not email or not password:
            if request.content_type == 'application/json':
                return Response({
                    'success': False,
                    'error': 'Email y contraseña son requeridos'
                }, status=status.HTTP_400_BAD_REQUEST)
            return render(request, 'login/login.html', {'error': 'Email y contraseña son requeridos'})

        # Autenticar usando email (USERNAME_FIELD = 'email')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)

            # Generar tokens JWT
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            # Si es petición JSON, responder con JSON y tokens
            if request.content_type == 'application/json':
                return Response({
                    'success': True,
                    'message': 'Login exitoso',
                    'access': access_token,
                    'refresh': refresh_token,
                    'redirect': '/dashboard/'
                }, status=status.HTTP_200_OK)
            return redirect('dashboard')
        else:
            if request.content_type == 'application/json':
                return Response({
                    'success': False,
                    'error': 'Credenciales inválidas'
                }, status=status.HTTP_400_BAD_REQUEST)
            return render(request, 'login/login.html', {'error': 'Credenciales inválidas'})


class LogoutUsuarios(APIView):

    @swagger_auto_schema(
        operation_description="Cerrar sesión",
        responses={302: 'Redirige al home'}
    )
    def get(self, request):
        logout(request)
        return redirect('home')