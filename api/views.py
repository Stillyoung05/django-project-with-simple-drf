from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import BookAuthorSerializer, BooksSerializer
from books.models import ReviewBookModel, BooksModel


class BookReviewAPIView(APIView):
    def get(self, request):
        books = ReviewBookModel.objects.all()
        serializer = BookAuthorSerializer(books,many=True)
        return Response(data=serializer.data)


class BookListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        books = BooksModel.objects.all()
        serializer = BooksSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



