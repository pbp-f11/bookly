from django.shortcuts import render
from django.http import HttpResponseRedirect
from edit_delete_book.forms import BookForm
from django.urls import reverse
from book.models import Book

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

def edit_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    forms = BookForm(request.POST or None, instance=book)
    if forms.is_valid() and request.method == 'POST':
        forms.save()
        return HttpResponseRedirect(reverse('edit_delete_book:show', args=(book_id,)))
    context = {
        'forms': forms,
    }
    return render(request, 'edit_book.html', context)
