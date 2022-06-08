from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic import FormView
from .forms import NewUserForm
from .Scrapper.Scrapper import get_rss_feeds
from .models import FeedArticle

# Good for using LoginRequiredMixin 👍
class HomeView(LoginRequiredMixin, TemplateView):
    login_url = "/users/auth/login"
    template_name = "index.html"

    def get(self, request: HttpRequest) -> HttpResponse:

        urls_to_scrape = [
            "http://www.nu.nl/rss/Algemeen",
            "https://feeds.feedburner.com/tweakers/mixed",
        ]
        # Why did you choose to use feedparser instead of building your own feed parser?
        context = {"feeds": get_rss_feeds(urls_to_scrape)}
        return render(request, self.template_name, context)
    

class RegisterUserView(FormView):
    template_name: str = "auth_templates/register.html"
    # FIXME: Replace NewUserForm to CreateUserForm (optional) using a verb as prefix is good for context
    form_class = NewUserForm

    def get(self, request: HttpRequest) -> HttpResponse:
        context = {"form": self.form_class()}

        return render(request, self.template_name, context)

    def post(self, request: HttpRequest) -> HttpResponse:
        form = NewUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")

        return redirect("register_user")

class BookmarksView(FormView):
    
    def post(self, request: HttpRequest) -> HttpResponse:
        title = request.POST.get('title')
        link = request.POST.get('link')
        summary = request.POST.get('summary')
        
        db_article = FeedArticle.objects.filter(title=title)
        
        if db_article.exists():
            feed_article = db_article[0]
            feed_article.bookmarks.add(request.user)
        else:
            feed_article = FeedArticle()
        
            feed_article.title = title
            feed_article.link = link
            feed_article.summary = summary
            feed_article.save()
            
            feed_article.bookmarks.add(request.user)
        
        return redirect("home")
