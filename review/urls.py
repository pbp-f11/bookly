from django.urls import path
from review.views import *

app_name = 'review'

urlpatterns = [
    path('create-review-ajax/<int:book_id>/', add_review_ajax, name='add_review_ajax'),
    path('get-review/<int:book_id>/', get_review_json, name='get_review_json'),
    path('show-reviews/<int:book_id>/', show_reviews, name='show_reviews'),
    path('add-review/<int:book_id>/', add_review, name='add_review'),
    path('show-reviews-specific-user/', show_reviews_specific_user, name='show_reviews_specific_user'),
    path('get-review-json-by-user-id/', get_review_json_by_user_id, name='get_review_json_by_user_id'),
    path('show-reviews-specific-user/edit-reviews/<int:book_id>/', edit_reviews, name='edit_reviews'),
    path('show-reviews-specific-user/delete-item-ajax/<int:review_id>', delete_item_ajax, name='delete_item_ajax'),
    path('show-reviews-specific-user/delete-item-flutter/', delete_item_flutter, name='delete_item_flutter'),
    path('show-reviews-specific-user/edit-review-flutter/', edit_review_flutter, name='delete_item_flutter'),
    path('add-review-flutter/<int:book_id>/', add_review_flutter, name='add_review_flutter'),
]