from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}


class UserRols(models.TextChoices):
    ADMIN = 'admin', _('admin')
    MODERATOR = 'moderator', _('moderator')
    USER = 'user', _('user')


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    role = models.CharField(max_length=9, choices=UserRols.choices, default=UserRols.USER)
    first_name = models.CharField(max_length=150, verbose_name='Имя', default='Аноним')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия', default='Аноним')
    phone = models.CharField(max_length=35, unique=True, verbose_name='phone_number', **NULLABLE)
    telegram = models.CharField(max_length=150, unique=True, verbose_name='telegram_user_name', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='active')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['id']
