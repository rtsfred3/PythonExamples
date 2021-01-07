from django.db import models

from apps.users.models import *

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    #last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books_uploaded")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)