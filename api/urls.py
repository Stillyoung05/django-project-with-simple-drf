from django.urls import path
from .views import BookReviewAPIView, BookListAPIView

urlpatterns = [
    path('review/', BookReviewAPIView.as_view(), name='review'),
    path('book-list/', BookListAPIView.as_view(), name='book-list'),

]
