from django.urls import path
from review.views import show_reviews, add_review, get_review_json, add_review_ajax, edit_review, \
    show_reviews_specific_user, get_review_json_by_user_id

app_name = 'review'

urlpatterns = [
    path('create-review-ajax/<int:book_id>/', add_review_ajax, name='add_review_ajax'),
    path('get-review/<int:book_id>/', get_review_json, name='get_review_json'),
    path('show-reviews/<int:book_id>/', show_reviews, name='show_reviews'),
    path('add-review/<int:book_id>/', add_review, name='add_review'),
    path('show-reviews-specific-user/', show_reviews_specific_user, name='show_reviews_specific_user'),
    path('get-review-json-by-user-id/', get_review_json_by_user_id, name='get_review_json_by_user_id'),
    path('edit-review/', edit_review, name='edit_review'),

]