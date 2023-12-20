from django.urls import path
from users.views import register, login_user, logout_user, get_user_review, show_profile_json

app_name = 'users'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('get_user_review/', get_user_review, name='get_user_review'),
    path('show_profile_json/', show_profile_json, name='show_profile_json'),
]