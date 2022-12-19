from django.contrib import admin

from product.models import Book, Comment, Genre, Rating, Reporter, Article


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('date', 'text')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Rating)
class Rating(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'in_stock')


@admin.register(Reporter)
class ReporterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('headline', 'pub_date', 'reporter')
