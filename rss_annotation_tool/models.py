from django.db import models
from django.contrib.auth.models import User

class FeedArticle(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    summary = models.TextField()
    comments = models.TextField(blank=True)
    bookmarks = models.ManyToManyField(User, 'Bookmarks')
    