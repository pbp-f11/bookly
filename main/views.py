from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
<<<<<<< HEAD

from book.models import Book

def show_main(request):
    books = Book.objects.all()
    context = {
=======
from django.contrib.auth.decorators import login_required

from book.models import Book

@login_required(login_url='/login')
def show_main(request):
    books = Book.objects.all()
    context = {
        'name': request.user.username,
>>>>>>> df92c05 (commit dbsqlite3 3rd time)
        'books': books
    }
    return render (request, "main.html", context)