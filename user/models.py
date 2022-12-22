from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models

from product.models import Rating, Comment, Book
from user.managers import CustomUserManager


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    username = None
    ratings = models.ForeignKey(Rating, related_name='user_id', on_delete=models.CASCADE, null=True, blank=True)
    comments = models.ForeignKey(Comment, related_name='user_id', on_delete=models.CASCADE, null=True, blank=True)
    favorites = models.ManyToManyField(Book)
    role = models.CharField(verbose_name='User role', max_length=10)
    email = models.EmailField(verbose_name='Your email', max_length=40, db_index=True, unique=True)
    name = models.CharField(verbose_name='Your name', max_length=30)
    password = models.CharField(verbose_name='Your password', max_length=255)
    avatar = models.CharField(verbose_name='Your avatar', max_length=250, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email
