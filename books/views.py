from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from books.models import Book, Review


# Create your views here.
def index(request):
    data = Book.objects.all()
    context = {"books": data}
    return render(request, "books/index.html", context)


def show(request, id):
    reviews = Review.objects.order_by('-created_at')
    single_book = get_object_or_404(Book, pk=id)
    context = {"book": single_book, "reviews": reviews}
    return render(request, "books/show.html", context)


def review(request):
    body = request.POST["review"]
    form = Review(body=body)
    form.save()
    return redirect("/")
