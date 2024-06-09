from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    phone = models.CharField(max_length=32, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/avatars/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=32, verbose_name='страна', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return f'{self.email}'
