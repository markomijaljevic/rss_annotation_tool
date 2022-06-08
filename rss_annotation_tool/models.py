from django.db import models
from django.contrib.auth.models import User

class FeedArticle(models.Model):
    title = models.CharField(max_length=255, primary_key=True)
    link = models.CharField(max_length=255)
    summary = models.TextField()
    comment = models.TextField()
    bookmarks = models.ManyToManyField(User, 'Bookmarks')