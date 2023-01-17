from django.contrib import admin

from product.models import Book, Comment, Genre, Rating


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('date', 'text')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Rating)
class Rating(admin.ModelAdmin):
    list_display = ('rating',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'in_stock')

