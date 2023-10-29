from django.db import models
from django.contrib.auth.models import User
from book.models import Book

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    full_name = models.CharField(max_length=255, null=True, default=None)
    address = models.CharField(max_length=255, null=True, default=None)
    phone_number = models.CharField(max_length=255, default=None)

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)