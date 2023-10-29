from django.db import models
from django.contrib.auth.models import User
from book.models import Book

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(null= True, default=None, blank=True)
    first_name = models.CharField(max_length=255, null=True, default=None, blank=True)
    last_name = models.CharField(max_length=255, null=True, default=None, blank=True)
    address = models.CharField(max_length=255, null=True, default=None, blank=True)
    phone_number = models.CharField(max_length=255, null=True, default=None, blank=True)
    
    LIST_GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    gender = models.CharField(max_length=255, null=True, choices=LIST_GENDER, default=None, blank=True)