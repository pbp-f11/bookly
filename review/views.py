import json
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse
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

def get_review_json_by_user_id(request):
    # book = Book.objects.get(pk=book_id)
    product_item = Review.objects.filter(user=request.user)
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

def show_reviews_specific_user(request):
    try:
        reviews = Review.objects.filter(user=request.user)
        context = {
            'reviews': reviews
        }
        return render(request, "show_reviews_specific_user.html", context)
    except Book.DoesNotExist:
        # Handle the case where the book does not exist
        # You can render an error page or return an appropriate response here
        pass

def edit_reviews(request, book_id):
    # Get product berdasarkan ID
    product = Review.objects.get(pk = book_id)

    # Set product sebagai instance dari form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('review:show_reviews_specific_user'))

    context = {'form': form}
    return render(request, "edit_reviews.html", context)

@csrf_exempt
def delete_item_ajax(request, review_id):
    if request.method == 'DELETE':
        product = get_object_or_404(Review, pk=review_id)
        product.delete()
        return HttpResponse(b"DELETED", status=204)
    return HttpResponseNotFound()

def delete_item_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product = get_object_or_404(Review, pk=data['review_id'])
        product.delete()
        return JsonResponse({"status": True}, status = 200)
    return JsonResponse ({"status": True}, status = 200)


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