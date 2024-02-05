from rest_framework import serializers
from books.models import ReviewBookModel, BooksModel


class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewBookModel
        fields = '__all__'


class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = BooksModel
        # fields = ('book_name', 'short_description', 'publisher',)
        fields = "__all__"


class BookDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = BooksModel
        fields = '__all__'

