from django.shortcuts import render
from add_book.forms import BookForm
from book.models import Book
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def get_book(request):
    book = Book.objects.all()
    return HttpResponse(serializers.serialize('json', book))

@csrf_exempt
def add_book(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        author = request.POST.get("author")
        price = request.POST.get("price")
        year = request.POST.get("year")
        genre = request.POST.get("genre")

        new_product = Book(name=name, author=author, price=price, year=year, genre=genre)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()