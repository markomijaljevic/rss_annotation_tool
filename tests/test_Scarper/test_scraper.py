from django.test import TestCase

from rss_annotation_tool.Scraper.Scraper import get_rss_feeds

class TestScraper(TestCase):
    
    def setUp(self) -> None:
        self.urls_to_scrape = [
            "http://www.nu.nl/rss/Algemeen",
            "https://feeds.feedburner.com/tweakers/mixed",
        ]
        
    def test_get_rss_feeds_all_fields_scraped_good(self):

        result = get_rss_feeds(self.urls_to_scrape)
        assert len(result) == len(self.urls_to_scrape)
        
    # def test_get_rss_feeds_entries_exist_good(self):
    #     result = get_rss_feeds(self.urls_to_scrape)
    #     assert 'entries' in result[0].keys()
    
    