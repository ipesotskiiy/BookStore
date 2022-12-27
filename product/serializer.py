from itertools import count

from rest_framework import serializers

from product.models import Comment, Genre, Rating, Book


class CommentSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(required=True)

    def validate(self, value):
        return value

    class Meta:
        model = Comment
        fields = (
            'date',
            'text',
            'bookId'
        )


class GenreSerializer(serializers.ModelSerializer):
    genreId = serializers.SerializerMethodField('get_id')

    class Meta:
        model = Genre
        fields = ('name', 'genreId')

    def get_id(self, obj):
        return obj.id


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    bookId = serializers.SerializerMethodField('get_id')
    comments = CommentSerializer(many=True)

    class Meta:
        depth = 1
        model = Book
        fields = (
            '__all__'
        )

    def comment_set2(self, obj):
        return []

    def get_id(self, obj):
        return obj.id


class BookRateSerializer(serializers.ModelSerializer):
    bookId = serializers.SerializerMethodField('get_id')
    average_rate = serializers.SerializerMethodField('calculate_average_rate_value')

    def calculate_average_rate_value(self, book):
        ratings = [item.name for item in Rating.objects.filter(bookId=book.bookId)]
        count_rate = len(ratings)
        sum_rate = sum(ratings)
        return sum_rate/count_rate

    def get_id(self, obj):
        return obj.bookId_id

    class Meta:
        model = Book
        fields = [
            'bookId',
            'average_rate'
        ]

