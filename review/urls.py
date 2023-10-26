from django.urls import path
from add_review.views import add_review

app_name = 'add_review'

urlpatterns = [
    path('', add_review, name='add_review'),
]