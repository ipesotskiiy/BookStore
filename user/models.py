from django.core.validators import RegexValidator
from django.db import models

from product.models import Rating, Comment, Book


# Create your models here.
class User(models.Model):
    ratings = models.ForeignKey(Rating, on_delete=models.CASCADE)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE)
    favorites = models.ForeignKey(Book, on_delete=models.CASCADE)
    role = models.CharField(verbose_name='User role', max_length=10)
    email = models.EmailField(verbose_name='Your email', max_length=40, db_index=True)
    name = models.CharField(verbose_name='Your name', max_length=30)
    password = models.CharField(verbose_name='Your password', max_length=255)
    avatar = models.ImageField(
        verbose_name='avatar',
        null=True,
        blank=True,
        default='images/anonim_user.jpg'
    )

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
