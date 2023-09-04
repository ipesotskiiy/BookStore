from rest_framework import serializers

from product.models import Comment, Genre, Rating, Book


class CommentSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(required=False, format="%Y-%m-%d %H:%M:%S")
    name = serializers.ReadOnlyField(source='user.name')
    avatar = serializers.ReadOnlyField(source='user.avatar')

    def validate(self, value):
        return value

    class Meta:
        model = Comment
        fields = (
            'date',
            'text',
            'bookId',
            'user',
            'name',
            'avatar'
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


class BookSerializer(serializers.ModelSerializer):
    bookId = serializers.SerializerMethodField('get_id')
    comments = CommentSerializer(many=True)
    ratings = RatingSerializer(many=True)
    averageRate = serializers.SerializerMethodField('get_rating')

    class Meta:
        depth = 1
        model = Book
        fields = (
            '__all__'
        )

    def get_rating(self, obj):
        ratings = [i.get('rating') for i in RatingSerializer(obj.ratings, many=True).data]
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


class FavoriteSerializer(serializers.ModelSerializer):
    isInFavorite = serializers.BooleanField(required=False)
    title = serializers.CharField(required=False)
    author = serializers.CharField(required=False)
    price = serializers.DecimalField(required=False, max_digits=8, decimal_places=2)

    class Meta:
        depth = 1
        model = Book
        fields = (
            '__all__'
        )
