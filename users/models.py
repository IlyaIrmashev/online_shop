from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(
        verbose_name='почта',
        unique=True
    )
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE )
    phone = models.CharField(max_length=15, verbose_name='телефон', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='страна')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

