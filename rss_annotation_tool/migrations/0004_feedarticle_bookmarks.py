# Generated by Django 4.0.4 on 2022-06-08 10:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rss_annotation_tool', '0003_feedarticle_delete_feed'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedarticle',
            name='bookmarks',
            field=models.ManyToManyField(related_name='Bookmarks', to=settings.AUTH_USER_MODEL),
        ),
    ]
