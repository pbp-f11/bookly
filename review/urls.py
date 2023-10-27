from django.urls import path
from review.views import add_review

app_name = 'review'

urlpatterns = [
    path('add-review/<int:book_id>/', add_review, name='add_review'),
]