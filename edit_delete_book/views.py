from django.shortcuts import render
from django.http import HttpResponseRedirect
from edit_delete_book.forms import BookForm
from django.urls import reverse
from book.models import Book

def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('book:book_list'))
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_delete_book/edit_book.html', {'form': form})

def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return HttpResponseRedirect(reverse('book:book_list'))
