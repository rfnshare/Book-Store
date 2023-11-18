from django.http import HttpResponse
from django.shortcuts import render
import json

booksData = open('C:\\Users\\abdullah.faroque\\PycharmProjects\\bitfumes\\bookstore\\books.json').read()
data = json.loads(booksData)


# Create your views here.
def index(request):
    context = {'books': data}
    return render(request, 'books/index.html', context)


def show(request, id):
    global da
    for book in data:
        if book['id'] == id:
            da = book
    return render(request, 'books/show.html', da)
