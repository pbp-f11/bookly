from django.db import models

# Create your models here.
from django.db import models

class Book(models.Model):
    name = models.TextField(null=True, blank=True)
    author = models.TextField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    reviews = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    genre = models.TextField(null=True, blank=True)