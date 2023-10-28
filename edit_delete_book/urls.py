from django.urls import path
from edit_delete_book.views import *

app_name = 'edit_delete_book'

urlpatterns = [
    path('show/<int:book_id>/', show, name='show'),
    path('edit/<int:book_id>/', edit_book, name='edit_book'),
]
