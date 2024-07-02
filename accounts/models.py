from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Añade los campos adicionales que necesites para el perfil de usuario
    # Por ejemplo:
    # bio = models.TextField(max_length=500, blank=True)
    # avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return self.user.username
