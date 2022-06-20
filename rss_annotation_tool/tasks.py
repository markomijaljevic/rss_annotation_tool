from celery import shared_task
from rss_annotation_tool.models import FeedArticle
from rss_annotation_tool.Scraper.Scraper import get_rss_feeds
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from rss_annotation_tool.celery import app

@app.task
def load_rss_articles_into_db():
    
    urls_to_scrape = [
        "http://www.nu.nl/rss/Algemeen",
        "https://feeds.feedburner.com/tweakers/mixed",
    ]
    
    feeds = get_rss_feeds(urls_to_scrape)

    for feed in feeds:
        for article in feed.entries:
            title =article.get("title", "")
            link = article.get("link", "")
            summary = article.get("summary", "")
            
            feed_article = FeedArticle()

            feed_article.title = title
            feed_article.link = link
            feed_article.summary = summary
            feed_article.save()

    return True

@shared_task
def add(x, y):
    return x + y


schedule, created = IntervalSchedule.objects.get_or_create(
    every=2,
    period=IntervalSchedule.MINUTES,
)

PeriodicTask.objects.get_or_create(
    interval=schedule,
    name='Importing feeds every 2 min',
    task='rss_annotation_tool.tasks.load_rss_articles_into_db',
)