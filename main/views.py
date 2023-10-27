from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required

from book.models import Book

@login_required(login_url='/login')
def show_main(request):
    books = Book.objects.all()
    context = {
        'name': request.user.username,
        'books': books
    }
    return render (request, "main.html", context)