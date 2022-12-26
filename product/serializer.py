from rest_framework import serializers

from product.models import Comment, Genre, Rating, Book, Article, Reporter


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
        fields = ('__all__')


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


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['headline', 'pub_date']


class ReporterSerializer(serializers.ModelSerializer):
    articles = serializers.PrimaryKeyRelatedField(many=True, queryset=Article.objects.all())

    class Meta:
        model = Reporter
        fields = ['first_name', 'last_name', 'email', 'articles']
