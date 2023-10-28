from django.urls import path
from edit_delete_book.views import edit_book, delete_book

app_name = 'edit_delete_book'

urlpatterns = [
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),
]
