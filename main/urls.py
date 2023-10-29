from django.urls import path
from main.views import show_main
from main.views import add_bookmark, delete_bookmark

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path("add-bookmark/<int:id>", add_bookmark, name="add_bookmark"),
    path("delete-bookmark/<int:id>", delete_bookmark, name="delete_bookmark")
]