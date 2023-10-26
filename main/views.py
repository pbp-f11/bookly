from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from book.models import Book

def show_main(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render (request, "main.html", context)