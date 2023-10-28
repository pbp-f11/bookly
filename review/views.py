from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from review.forms import ProductForm
from django.urls import reverse
from review.models import Review
from book.models import Book
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from users.models import User


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
    # user = User.objects.filter(user=request.user)

    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            return HttpResponseRedirect(reverse('review:show_reviews', kwargs={'book_id': book_id}))
    else:
        form = ProductForm()

    context = {'form': form, 'book': book}
    return render(request, "add_review.html", context)


def get_review_json(request, book_id):
    book = Book.objects.get(pk=book_id)
    product_item = Review.objects.filter(book=book)
    return HttpResponse(serializers.serialize('json', product_item, use_natural_foreign_keys=True, use_natural_primary_keys=True))


@csrf_exempt
def add_review_ajax(request, book_id):
    if request.method == 'POST':
        book = Book.objects.get(pk=book_id)
        rating = request.POST.get("rating")
        reviews = request.POST.get("reviews")
        user = request.user

        new_review = Review(rating=rating, reviews=reviews, book=book, user=user)
        new_review.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
