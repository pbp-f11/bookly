import json
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.views.decorators.http import require_http_methods
from edit_delete_book.forms import BookForm
from django.urls import reverse
from book.models import Book
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core import serializers

from review.models import Review

def show(request, book_id):
    book = Book.objects.get(pk=book_id)
    forms = BookForm(request.POST or None, instance=book)
    context = {
        'book': book,
        'forms': forms,
    }
    return render(request, 'show.html', context)

def get_book_json(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        # Handle the case where the book doesn't exist
        return HttpResponseNotFound("Book not found")

    # Serialize the book data
    serialized_book = serializers.serialize('json', [book])

    # Convert the serialized data to a Python dictionary
    book_data = serialized_book[1:-1]  # Remove square brackets from serialized data
    book_dict = json.loads(book_data)

    # Return the book data as JSON response
    return JsonResponse(book_dict)

def get_review_json(request, book_id):
    book = Book.objects.get(pk=book_id)
    product_item = Review.objects.filter(book=book)
    return HttpResponse(serializers.serialize('json', product_item, use_natural_foreign_keys=True, use_natural_primary_keys=True))

@csrf_exempt
def edit_book(request, book_id):
    # Temukan buku berdasarkan ID
    book = Book.objects.get(pk=book_id)

    if request.method == 'POST':
        # Ambil data yang dikirim dari form
        name = request.POST.get('name')
        author = request.POST.get('author')
        price = request.POST.get('price')
        year = request.POST.get('year')
        genre = request.POST.get('genre')

        # Update atribut-atribut buku
        book.name = name
        book.author = author
        book.price = price
        book.year = year
        book.genre = genre

        # Simpan perubahan
        book.save()

        # Kirim respons JSON sebagai konfirmasi
        response_data = {
            'message': 'Detail buku berhasil diperbarui.',
        }
        return JsonResponse(response_data)
    
@csrf_exempt
def delete_book_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product = get_object_or_404(Review, pk=data['review_id'])
        product.delete()
        return JsonResponse({"status": True}, status = 200)
    return JsonResponse ({"status": True}, status = 200)

@csrf_exempt
@require_http_methods(["PUT"])
def edit_book_flutter(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        # Handle the case where the book doesn't exist
        return JsonResponse({"error": "Book not found"}, status=404)

    if request.method == 'PUT':
        data = request.body.decode('utf-8')
        book_data = json.loads(data)

        # Update atribut-atribut buku dengan data yang diterima dari Flutter
        if 'name' in book_data:
            book.name = book_data['name']
        if 'author' in book_data:
            book.author = book_data['author']
        if 'price' in book_data:
            book.price = book_data['price']
        if 'year' in book_data:
            book.year = book_data['year']

        # Simpan perubahan
        book.save()

        # Kirim respons JSON sebagai konfirmasi
        return JsonResponse({"message": "Book details updated successfully"})

    return JsonResponse({"error": "Invalid request method"}, status=400)