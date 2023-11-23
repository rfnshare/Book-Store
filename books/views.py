from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from books.models import Book


# Create your views here.
def index(request):
    data = Book.objects.all()
    context = {'books': data}
    return render(request, 'books/index.html', context)


def show(request, id):
    single_book = get_object_or_404(Book, pk=id)
    context = {'book': single_book}
    return render(request, 'books/show.html', context)
