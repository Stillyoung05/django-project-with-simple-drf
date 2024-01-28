from django.shortcuts import render,redirect,get_object_or_404
from .models import BooksModel
from .forms import UpdateBookForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def books_view(request):
    books = BooksModel.objects.order_by('book_name')
    context = {
        'books':books
    }
    return render(request,'books/book.html',context=context)

@login_required
def update_book(request, pk):
    book_instance = get_object_or_404(BooksModel, pk=pk)

    if request.method == 'POST':
        form = UpdateBookForm(request.POST, request.FILES, instance=book_instance)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = UpdateBookForm(instance=book_instance)

    return render(request, 'books/update_book.html', {'form': form,'book':book_instance})

@login_required
def delete_book(request, pk):
    book_instance = get_object_or_404(BooksModel, pk=pk)

    if request.method == 'POST':
        book_instance.delete()
        return redirect('books')

    return render(request, 'books/delete.html', {'book': book_instance})

@login_required
def about_book(request,pk):
    book = BooksModel.objects.get(pk=pk)
    context = {
        'book':book,
    }
    return render(request,'books/about_book.html',context=context)