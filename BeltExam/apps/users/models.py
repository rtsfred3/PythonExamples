from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Quote(models.Model):
    quote = models.TextField()
    author = models.TextField()
    submitter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="quotes_submitted", null=True)
    created_at = models.DateTimeField(auto_now_add = True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes", null=True)
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE, related_name="likes", null=True)