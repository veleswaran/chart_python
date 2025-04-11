from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.Case)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

