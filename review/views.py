from django.shortcuts import render
from django.http import HttpResponseRedirect
from review.forms import ProductForm
from django.urls import reverse
from review.models import Review
from book.models import Book


# Create your views here.

def show_reviews(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
        reviews = Review.objects.filter(book=book)
        context = {
            'book': book,
            'reviews': reviews
        }
        return render(request, "show_reviews.html", context)
    except Book.DoesNotExist:
        # Handle the case where the book does not exist
        # You can render an error page or return an appropriate response here
        pass

def add_review(request, book_id):
    # Get the book object based on the book_id
    book = Book.objects.get(pk=book_id)

    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.save()
            return HttpResponseRedirect(reverse('review:show_reviews', kwargs={'book_id': book_id}))
    else:
        form = ProductForm()

    context = {'form': form, 'book': book}
    return render(request, "add_review.html", context)