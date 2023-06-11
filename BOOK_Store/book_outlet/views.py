from django.shortcuts import render
from .models import Book
from django.http import Http404
# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(request, "index.html", {"books": books})

def book_detail(request, slug):
    try:
        book = Book.objects.get(slug=slug)
    except:
        raise Http404()
    return render(request, "book_detail.html", {"book": book})    