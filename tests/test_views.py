from django.test import RequestFactory, TestCase
from rss_annotation_tool.views import HomeView

class TestViews(TestCase):
    
    def setup_view(self, view, request, *args, **kwargs):
        """
        Mimic ``as_view()``, but returns view instance.
        Use this function to get view instances on which you can run unit tests,
        by testing specific methods.
        """

        view.request = request
        view.args = args
        view.kwargs = kwargs
        return view
        
    def test_get_good(self):

        factory = RequestFactory()
        request = factory.get('/')
        
        view = self.setup_view(HomeView(), request)
        import pdb;pdb.set_trace()