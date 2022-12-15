from django.db import models
from django.utils import timezone


class Comment(models.Model):
    date = models.DateField(verbose_name='Comment date')
    text = models.TextField(verbose_name='Comment', max_length=900)


class Genre(models.Model):
    name = models.CharField(verbose_name='Genre', max_length=20)


class Rating(models.Model):
    name = models.FloatField(verbose_name='Rating', max_length=3)


class Book(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Book title', max_length=50)
    author = models.CharField(verbose_name='Author', max_length=80)
    price = models.DecimalField(verbose_name='Price', max_digits=8, decimal_places=2)
    cover = models.CharField(verbose_name='Cover', max_length=15, null=True, blank=True)
    date_of_issue = models.DateField(verbose_name='Date of Issue', default=timezone.now)
    in_stock = models.PositiveIntegerField(verbose_name='In stock', null=True, blank=True)
    description = models.TextField(verbose_name='Description', max_length=900, null=True, blank=True)
    average_rate = models.FloatField(verbose_name='Average rate', null=True, blank=True, max_length=3)
    is_in_favorite = models.BooleanField()

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'