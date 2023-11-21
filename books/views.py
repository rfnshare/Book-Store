from django.http import HttpResponse
from django.shortcuts import render
from books.models import Book


# Create your views here.
def index(request):
    data = Book.objects.all()
    context = {'books': data}
    return render(request, 'books/index.html', context)


def show(request, id):
    single_book = Book.objects.get(pk=id)
    context = {'book': single_book}
    return render(request, 'books/show.html', context)
