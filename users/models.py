from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    SUBSCRIBER = 'subscriber'
    AUTHOR = 'author'


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    role = models.CharField(max_length=20, choices=UserRoles.choices, default=UserRoles.SUBSCRIBER)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
