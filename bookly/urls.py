"""
URL configuration for bookly project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/', include("book.urls")),
    path('add_book/', include("add_book.urls")),
    path('edit_book/', include("edit_delete_book.urls")),
    path('', include("main.urls")),
    path('review/', include("review.urls")),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('login/', user_views.login_user, name='login'),
    path('register/', user_views.register, name='register'),
    path('logout/', user_views.logout_user, name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('user-review/', user_views.show_user_review, name='user-review'),
    path('auth/', include('authentication.urls')),
    path('profile-json/', user_views.show_profile_json, name='profile-json'),
    path('update-profile/', user_views.update_profile_flutter, name='update-profile'),
    path('get-user-review/', user_views.get_user_review, name='get-user-review')
]
