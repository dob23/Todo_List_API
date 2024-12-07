import hashlib
from django.contrib.auth.backends import ModelBackend
from user.models import User

class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            
            user = User.objects.filter(username=username).first()
            if user and user.check_password(password):
                return user
            
            
            psw_encrypted = hashlib.md5(password.encode()).hexdigest()
            if user and user.password == psw_encrypted:
                return user

            
            return None
        except Exception as e:
            print(f"Error durante la autenticación: {e}")
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
