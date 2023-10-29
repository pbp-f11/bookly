from django.db import models
from django.contrib.auth.models import User
from book.models import Book
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width  > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)