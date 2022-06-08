from django.test import TestCase

from rss_annotation_tool.views import HomeView

class TestViews(TestCase):
        
    def test_get_good(self):
        request = self.client.get('')
        view = HomeView()
        view.setup(request)
        
        print(view.get_context_data()['view'].__dict__)
        # context = view.get_context_data()