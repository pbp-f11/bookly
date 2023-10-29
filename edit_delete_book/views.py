from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from edit_delete_book.forms import BookForm
from django.urls import reverse
from book.models import Book
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core import serializers

def show(request, book_id):
    book = Book.objects.get(pk=book_id)
    forms = BookForm(request.POST or None, instance=book)
    if forms.is_valid() and request.method == 'POST':
        forms.save()
        return HttpResponseRedirect(reverse('edit_delete_book:show', args=(book_id,)))
    context = {
        'book': book,
        'forms': forms,
    }
    return render(request, 'show.html', context)

def get_book(request):
    book = Book.objects.all()
    return HttpResponse(serializers.serialize('json', book))

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
def delete_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()
    return HttpResponseRedirect('/book/')

def get_book(request, book_id):
    book = Book.objects.get(id=book_id)
    return HttpResponse(serializers.serialize("json", book), content_type="application/json")