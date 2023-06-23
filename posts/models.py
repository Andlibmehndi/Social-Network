from django.db import models
from django.contrib.auth import get_user_model

class Post(models.Model):
    User = get_user_model()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    description = models.TextField()
    like = models.ManyToManyField(to=User, related_name='liked_posts', blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)