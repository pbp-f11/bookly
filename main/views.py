from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers


from book.models import Book

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.urls import reverse
from book.models import Book
from users.models import Bookmark 

@login_required(login_url='/login')
def show_main(request):
    books = Book.objects.all()
    context = {
        'name': request.user.username,
        'books': books
    }
    return render (request, "main.html", context)

def add_bookmark(request, id):
    book = Book.objects.get(pk=id)
    Bookmark.objects.create(user=request.user, book=book)
    return HttpResponseRedirect(reverse("main:show_main"))


def delete_bookmark(request, id):
    book = Book.objects.get(pk=id)
    bookmark = Bookmark.objects.filter(user=request.user, book=book)
    bookmark.delete()
    return HttpResponseRedirect(reverse("main:show_main"))