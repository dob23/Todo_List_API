from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
# Create your views here.
class LoginView(APIView):
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        if not username or not password:
            raise AuthenticationFailed('Debe Proporcionar un usuario y una contraseña')
        
        user = authenticate(request, username, password = password)
        
        if user is None:
            raise AuthenticationFailed('Credenciales Incorrectas')
        
        return Response({
            'message': 'Autenticacion exitosa',
            'user': {
                'username': user.username,
                'email': user.email,
            }
        })