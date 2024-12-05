from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class authBackends(BaseBackend):
    def authenticate(self,request, username=None,password=None):
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user 
            else:
                raise ValidationError("Contraseña Incorecta")
        except User.DoesNotExist:
            raise ValidationError("Usuario no encontrado")
    def get_user(self,user_id):
        try: 
            return User.Objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
        
        
