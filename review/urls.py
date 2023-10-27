from django.urls import path
from review.views import show_reviews, add_review, get_review_json, add_review_ajax

app_name = 'review'

urlpatterns = [
    path('create-review-ajax/<int:book_id>/', add_review_ajax, name='add_review_ajax'),
    path('get-review/<int:book_id>/', get_review_json, name='get_review_json'),
    path('show-reviews/<int:book_id>/', show_reviews, name='show_reviews'),
    path('add-review/<int:book_id>/', add_review, name='add_review'),
]