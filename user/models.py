from django.core.validators import RegexValidator
from django.db import models

from product.models import Rating, Comment, Book


# Create your models here.
class User(models.Model):
    ratings = models.ForeignKey(Rating, on_delete=models.CASCADE)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(Book)
    role = models.CharField(verbose_name='User role', max_length=10)
    email = models.EmailField(verbose_name='Your email', max_length=40, db_index=True)
    name = models.CharField(verbose_name='Your name', max_length=30)
    password = models.CharField(verbose_name='Your password', max_length=255)
    avatar = models.CharField(verbose_name='Your avatar', max_length=250, null=True, blank=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
