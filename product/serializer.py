from itertools import count

from django.utils import timezone
from rest_framework import serializers

from product.models import Comment, Genre, Rating, Book


class CommentSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(required=False, format="%Y-%m-%d %H:%M:%S")

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


class RateSerializer(serializers.ModelSerializer):
    # bookId = serializers.SerializerMethodField('get_id')
    # averageRate = serializers.SerializerMethodField('calculate_average_rate_value')

    def calculate_average_rate_value(self, book):
        ratings = [item.name for item in Rating.objects.filter(bookId=book.bookId_id)]
        count_rate = len(ratings)
        sum_rate = sum(ratings)
        return sum_rate / count_rate

    def get_id(self, obj):
        return obj.bookId_id

    class Meta:
        model = Rating
        fields = (
            # 'bookId',
            # 'averageRate',
            # 'name'
            '__all__'
        )


class BookSerializer(serializers.ModelSerializer):
    bookId = serializers.SerializerMethodField('get_id')
    comments = CommentSerializer(many=True)
    rating = RateSerializer(many=True)
    averageRate = serializers.SerializerMethodField('get_rating')
    # averageRate = BookRateSerializer(many=True)

    class Meta:
        depth = 1
        model = Book
        fields = (
            '__all__'
        )

    def get_rating(self, obj):
        ratings = [i.get('name') for i in RateSerializer(obj.rating, many=True).data]
        len_rat = len(ratings)
        sum_rat = sum(ratings)
        if len_rat == 0 or sum_rat == 0:
            return 0

        average_rate = sum_rat/len_rat
        if average_rate > 5:
            average_rate = 5
        return average_rate

    def get_id(self, obj):
        return obj.id


class BookRateSerializer(BookSerializer):
    # bookId = serializers.SerializerMethodField('get_id')
    averageRate = serializers.SerializerMethodField('calculate_average_rate_value')

    def calculate_average_rate_value(self, book):
        a = 2
        ratings = [item.name for item in Rating.objects.filter(bookId=book.bookId_id)]
        count_rate = len(ratings)
        sum_rate = sum(ratings)
        return sum_rate / count_rate

    def get_id(self, obj):
        return obj.bookId_id

    class Meta:
        model = Book
        fields = '__all__'
