# Generated by Django 4.0.4 on 2022-06-16 13:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('summary', models.TextField()),
                ('comments', models.TextField(blank=True)),
                ('bookmarks', models.ManyToManyField(related_name='Bookmarks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
