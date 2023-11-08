from django.urls import path
from add_book.views import *

app_name = 'add_book'

urlpatterns = [
    path('get_book/', get_book, name='get_book'),
    path('add_book/', add_book, name='add_book')
]