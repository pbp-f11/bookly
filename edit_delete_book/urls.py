from django.urls import path
from edit_delete_book.views import *

app_name = 'edit_delete_book'

urlpatterns = [
    path('show/<int:book_id>/', show, name='show'),
    path('edit/<int:book_id>/', edit_book, name='edit_book'),
    path('get_book_json/<int:book_id>/', get_book_json, name='get_book_json'),
    path('delete_book_flutter/', delete_book_flutter, name='delete_book_flutter'),
    path('edit_book_flutter/<int:book_id>', edit_book_flutter, name='edit_book_flutter'),
]