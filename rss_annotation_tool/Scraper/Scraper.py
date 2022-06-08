from typing import List
import feedparser


def get_rss_feeds(urls) -> List[feedparser.FeedParserDict]:

    feeds = []

    for url in urls:
        feed_dict = feedparser.parse(url)
        feeds.append(feed_dict)

    return feeds
