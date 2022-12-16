from rest_framework import serializers

from product.models import Comment, Genre, Rating, Book


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('date', 'text')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name',)


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('name',)


class BookSerializer(serializers.ModelSerializer):
    bookId = serializers.SerializerMethodField('get_id')
    class Meta:

        model = Book
        fields = (
            'comment',
            'genre',
            'rating',
            'title',
            'author',
            'price',
            'cover',
            'date_of_issue',
            'in_stock',
            'description',
            'average_rate',
            'is_in_favorite',
            'id',
            'bookId'
        )

    def get_id(self, obj):
        return obj.id
