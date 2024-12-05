from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views import View

class LoginView(View):
    template_name = 'loginUP.html'

    def get(self, request, *args, **kwargs):
        """
        Renderiza el formulario de inicio de sesión si el usuario no está autenticado.
        """
        if request.user.is_authenticated:
            return redirect('/') 
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        """
        Procesa el inicio de sesión del usuario.
        """
        username = request.POST.get('username')
        password = request.POST.get('password')

      
        if not username or not password:
            return render(request, self.template_name, {
                'error': 'Debe proporcionar un usuario y una contraseña.'
            })

       
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, self.template_name, {
                'error': 'Credenciales incorrectas. Intente de nuevo.'
            })

       
        login(request, user)
        return redirect('/') 


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        """
        Cierra la sesión del usuario y redirige al login.
        """
        logout(request)
        return redirect('/login/')
