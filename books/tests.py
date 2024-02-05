from django.test import TestCase,Client
from django.urls import reverse
from books.models import BooksModel,AuthorModel,BookAuthorModel,ReviewBookModel
import json
from decimal import Decimal

# Create your tests here.

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('books')
        self.detail_url = reverse('update',args=[1])
        self.book_name = BooksModel.objects.create(
            book_name = 'book_name',
            book_price =Decimal('1234.00')
        )
        

    def test_books_views_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'books/book.html')

    def test_update_views_GET(self):
        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'books/update_book.html')