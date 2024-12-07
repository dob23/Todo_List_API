from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    profile = models.CharField(max_length=150, verbose_name='Perfil', blank=True)
    registro_interno = models.IntegerField(default=0, verbose_name='Registro Interno')
    date_joined = models.DateTimeField(null = True , blank=True)

    def __str__(self):
        return self.username
