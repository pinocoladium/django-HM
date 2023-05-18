from django.shortcuts import render, redirect
import datetime
from .models import Book

def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    all_books = Book.objects.all()
    context = {
        'books': all_books
    }
    return render(request, template, context)

def book_view_show(request, get_pub_date):
    template = 'books/book_list.html'
    book = Book.objects.get(pub_date=get_pub_date)
    content = list(Book.objects.all().order_by('pub_date'))
    prev_book = content[content.index(book) - 1]
    if content.index(book) + 1 == len(content):
        next_book = content[0]
    else:
        next_book = content[content.index(book) + 1]
    context = {
        'book': book,
        'next_book': next_book,
        'prev_book': prev_book,
        }
    return render(request, template, context)