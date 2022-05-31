from typing import List
import feedparser


class RSScrapper:
    def __init__(self, urls: List[str] = []) -> None:
        self.urls = urls

    def get_rss_feeds(self) -> List[feedparser.FeedParserDict]:

        feeds = []

        for url in self.urls:
            feed_dict = feedparser.parse(url)
            feeds.append(feed_dict)

        return feeds
