from django.urls import path
from .views import books_view,about_book,update_book,delete_book,add_comment

urlpatterns = [
    path('books/',books_view,name='books'),
    path('<int:pk>/about-book/',about_book,name='book'),
    path('update/<int:pk>/',update_book,name='update'),
    path('delete/<int:pk>/',delete_book,name='delete'),
    path('add/comment/',add_comment,name='add_comment'),
]