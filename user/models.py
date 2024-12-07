from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    """
    Modelo personalizado de usuario que hereda de AbstractUser.
    Se agregan campos adicionales y se personalizan los nombres inversos
    para evitar conflictos con los modelos predeterminados de Django.
    """
    profile = models.CharField(
        max_length=150,
        verbose_name='Perfil',
        blank=True,
        help_text="Perfil del usuario (ej. admin, supervisor, etc.)."
    )
    registro_interno = models.IntegerField(
        default=0,
        verbose_name='Registro Interno',
        help_text="Número de registro interno único para el usuario."
    )
    date_joined = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Fecha de Registro',
        help_text="Fecha en la que el usuario se unió al sistema."
    )

    # Relación con grupos (ManyToMany con nombre inverso personalizado)
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # Nombre inverso personalizado
        verbose_name="Grupos",
        blank=True,
        help_text="Grupos a los que pertenece el usuario."
    )

    # Relación con permisos (ManyToMany con nombre inverso personalizado)
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions_set",  # Nombre inverso personalizado
        verbose_name="Permisos",
        blank=True,
        help_text="Permisos asignados al usuario."
    )

    def __str__(self):
        """
        Devuelve una representación legible del usuario.
        """
        return self.username

    class Meta:
        """
        Metadatos del modelo.
        """
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
