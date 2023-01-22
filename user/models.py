from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from user.managers import CustomUserManager


def upload_to(instance, filename):
    return 'media/images/{filename}'.format(filename=filename)


class User(AbstractBaseUser, PermissionsMixin):
    username = None
    favorites = models.ManyToManyField('product.Book', null=True, blank=True, related_name='favorites')
    role = models.CharField(verbose_name='User role', max_length=10, null=True, blank=True)
    email = models.EmailField(verbose_name='Your email', max_length=40, db_index=True, unique=True)
    name = models.CharField(verbose_name='Your name', max_length=30, null=True, blank=True)
    password = models.CharField(verbose_name='Your password', max_length=255)
    avatar = models.FileField(
        upload_to='',
        verbose_name='Your avatar',
        max_length=250,
        null=True,
        blank=True
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email
