from rest_framework import serializers

from product.models import Comment, Genre, Rating, Book, Article, Reporter


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            '__all__'
        )
        # 'text',
        # 'bookId')


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
        fields = ('name',)


class BookSerializer(serializers.ModelSerializer):
    bookId = serializers.SerializerMethodField('get_id')
    comments = CommentSerializer(many=True)

    # genres = GenreSerializer(many=True)

    # genres = GenreSerializer(many=True)
    class Meta:
        depth = 1
        model = Book
        fields = (
            '__all__'
        )
        #     'comments',
        #     'genre',
        #     'title',
        #     'author',
        #     'price',
        #     'cover',
        #     'date_of_issue',
        #     'in_stock',
        #     'description',
        #     'average_rate',
        #     'is_in_favorite',
        #     'id',
        #     'bookId'
        # )

    def comment_set2(self, obj):
        return []

    def get_id(self, obj):
        return obj.id


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['headline', 'pub_date']


class ReporterSerializer(serializers.ModelSerializer):
    # articles = ArticleSerializer(many=True, read_only=True, q)
    articles = serializers.PrimaryKeyRelatedField(many=True, queryset=Article.objects.all())

    class Meta:
        model = Reporter
        fields = ['first_name', 'last_name', 'email', 'articles']
