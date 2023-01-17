from itertools import count

from django.utils import timezone
from rest_framework import serializers

from product.models import Comment, Genre, Rating, Book
# from user.serializer import UserSerializer


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
    rating = serializers.IntegerField(required=False)

    class Meta:
        model = Rating
        fields = '__all__'


class RateSerializer(serializers.ModelSerializer):
    # bookId = serializers.SerializerMethodField('get_id')
    # averageRate = serializers.SerializerMethodField('calculate_average_rate_value')

    def calculate_average_rate_value(self, book):
        ratings = [item.rating for item in Rating.objects.filter(bookId=book.bookId_id)]
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
    ratings = RateSerializer(many=True)
    averageRate = serializers.SerializerMethodField('get_rating')
    # user = UserSerializer(required=False, many=True)

    # averageRate = BookRateSerializer(many=True)

    class Meta:
        depth = 1
        model = Book
        fields = (
            '__all__'
        )

    def get_rating(self, obj):
        ratings = [i.get('rating') for i in RateSerializer(obj.ratings, many=True).data]
        len_rat = len(ratings)
        sum_rat = sum(ratings)
        if len_rat == 0 or sum_rat == 0:
            return 0

        average_rate = sum_rat / len_rat
        if average_rate > 5:
            average_rate = 5
        round_aver_rate = round(average_rate, 1)
        return round_aver_rate

    def get_id(self, obj):
        return obj.id


class BookRateSerializer(BookSerializer):
    averageRate = serializers.SerializerMethodField('calculate_average_rate_value')

    def calculate_average_rate_value(self, book):
        ratings = [item.rating for item in Rating.objects.filter(bookId=book.bookId_id)]
        for i in range(len(ratings)):
            if ratings[i] is None:
                ratings[i] = 1
        count_rate = len(ratings)
        sum_rate = sum(ratings)
        aver_rate = sum_rate / count_rate
        return round(aver_rate, 2)

    def get_id(self, obj):
        return obj.bookId_id

    class Meta:
        model = Book
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    isInFavorite = serializers.BooleanField(required=False)
    title = serializers.CharField(required=False)
    author = serializers.CharField(required=False)
    price = serializers.DecimalField(required=False, max_digits=8, decimal_places=2)
    genre = serializers.CharField(required=False)
    # user = UserSerializer(many=True, required=False)

    class Meta:
        depth = 1
        model = Book
        fields = (
            '__all__'
        )
