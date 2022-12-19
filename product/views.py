from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Book, Genre
from product.serializer import BookSerializer, GenreSerializer


# Create your views here.

class BookView(APIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    depth = 2

    # def get(self, request):
    #
    # #     serializer = BookSerializer(Book.objects.all())
    # #     return Response({"books": serializer.data})

    def get(self, request):
        books = Book.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = BookSerializer(books, many=True)
        return Response({"books": serializer.data})

class GenreView(APIView):
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



