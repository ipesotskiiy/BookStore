from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters, generics

from product.filters import PriceFilter
from product.models import Book, Genre
from product.serializer import BookSerializer, GenreSerializer


# Create your views here.
class GenreView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name']
    def get(self, request):
        queryset = Genre.objects.all()
        serializer = GenreSerializer(queryset, many=True)
        return Response({'genres': serializer.data})


class OneBookView(APIView):
    def get(self, request, id):
        queryset = Book.objects.get(pk=self.kwargs['id'])
        serializer = BookSerializer(queryset)
        # print(queryset[0].comment_set)
        return Response({"book": serializer.data})


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

    # def list(self, request):
    #     queryset = Book.objects.all()
    #     serializer = BookSerializer(queryset, many=True)
    #     return Response(serializer.data)


class BookView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['price', 'title', 'comments__id', 'genre__id']
    search_fields = ['price', 'title', 'comments__text']
    ordering_fields = ['title', 'id']
    ordering = ['title']

    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['genre', 'comments', 'price']
    # search_fields = ['=genre', 'comments', 'price']


    def get(self, request):
        books_qs = self.filter_queryset(Book.objects.all())
        serializer = BookSerializer(books_qs, many=True)
        # the many param informs the serializer that it will be serializing more than a single article.
        return Response({"books": serializer.data})



