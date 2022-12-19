from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Book
from product.serializer import BookSerializer


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


class OneBookView(APIView):
    def get(self, request, id):
        queryset = Book.objects.all() #filter(pk=self.kwargs['id'])
        serializer = BookSerializer(queryset, many=True)
        # print(queryset[0].comment_set)
        return Response({"book": serializer.data})
