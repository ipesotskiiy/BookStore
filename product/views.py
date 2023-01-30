from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters, generics

from product.filters import GenreAndPriceFilter
from product.models import Book, Genre, Comment, Rating
from product.serializer import (
    BookSerializer,
    GenreSerializer,
    CommentSerializer,
    RatingSerializer,
    BookRateSerializer,
    FavoriteSerializer
)
from user.serializer import UserSerializer

import random


class GenreView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name']

    def get(self, request):
        queryset = Genre.objects.all()
        serializer = GenreSerializer(queryset, many=True)
        return Response({'genres': serializer.data})


class CreateRatingView(generics.CreateAPIView):
    serializer_class = RatingSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'name': str(serializer.data)})
        else:
            return Response({'invalid': 'Invalid rating'})


class AverRateView(generics.ListAPIView):
    def get(self, request, id):
        name = Rating.objects.filter(bookId=self.kwargs['id'])
        serializer = BookRateSerializer(name, many=True)
        return Response({'aver_rate': serializer.data})


class OneBookView(APIView):
    def get(self, request, id):
        book = Book.objects.get(pk=self.kwargs['id'])
        book_serializer = BookSerializer(book)
        return Response({
            "book": book_serializer.data,
        })


class OneGenreView(APIView):

    def get(self, request, id):
        queryset = Genre.objects.get(pk=self.kwargs['id'])
        serializer = GenreSerializer(queryset)
        return Response({'genre': serializer.data})


class BookVS(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['price', 'title']
    search_fields = ['price', 'title']
    ordering_fields = ['title', 'id']
    ordering = ['title']


class BookView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = GenreAndPriceFilter
    filterset_fields = ['price', 'title', 'comments__id', 'genre__id']
    search_fields = ['price', 'title', 'comments__text']
    ordering_fields = ['title', 'id', 'price', 'author', 'date_of_issue', 'averageRate']
    ordering = ['title', 'price', 'author', 'date_of_issue', 'averageRate']

    def get(self, request):
        books_qs = self.filter_queryset(Book.objects.all())
        serializer = BookSerializer(books_qs, many=True)
        return Response({"books": serializer.data})


class CreateCommentView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def post(self, request, *args, **kwargs):
        name = request.user.name
        avatar = request.user.avatar
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            comment = serializer.save()
            return Response({'comment': CommentSerializer(comment).data})
        else:
            return Response({'invalid': 'Invalid comment'})


class RecommendationView(generics.ListAPIView):

    def get(self, request, id):
        books_without_excluded = Book.objects.exclude(id=self.kwargs['id']).all()

        [book1, book2] = random.sample(list(books_without_excluded), k=2)
        recommendation1 = BookSerializer(book1).data
        recommendation2 = BookSerializer(book2).data
        return Response(
            [recommendation1, recommendation2]
        )


class FavoritesView(generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = FavoriteSerializer

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user).data['favorites']
        return Response(serializer)

    def post(self, request, id, *args, **kwargs):
        user = request.user
        user.favorites.add(id)
        return Response(UserSerializer(user).data)

    def delete(self, request, id, *args, **kwargs):
        user = request.user
        user.favorites.remove(id)
        return Response(UserSerializer(user).data)
