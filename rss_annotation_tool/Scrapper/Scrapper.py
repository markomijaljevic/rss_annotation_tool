from typing import List
import feedparser

# TODO: Replace Scrapper to Scraper
#  why did you decided to create a class here?
#  when you could have created a method taking urls as input and returning the feeds


def get_rss_feeds(urls) -> List[feedparser.FeedParserDict]:

    feeds = []

    for url in urls:
        feed_dict = feedparser.parse(url)
        feeds.append(feed_dict)

    return feeds
