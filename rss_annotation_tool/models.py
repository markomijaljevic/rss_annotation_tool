from django.db import models
from django.contrib.auth.models import User

class FeedArticle(models.Model):
    # maybe composite key to make sure that feed article is the same.
    title = models.CharField(max_length=255, primary_key=True)
    link = models.CharField(max_length=255)
    summary = models.TextField()
    comments = models.TextField(blank=True)
    bookmarks = models.ManyToManyField(User, 'Bookmarks')