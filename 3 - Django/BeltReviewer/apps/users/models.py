from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class Review(models.Model):
    from apps.books.models import Book
    
    rating = models.IntegerField(default=0)
    review = models.TextField()
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews_posted", null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews_received")
    created_at = models.DateTimeField(auto_now_add = True)