from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# Classe de usuários

class Users(AbstractUser):
    choices_cargo = (('V','Vendedor'),
                     ('G', 'Gerente'))
    cargo = models.CharField(max_length= 1, choices=choices_cargo)