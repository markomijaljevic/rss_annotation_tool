from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.views import LoginView

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic import FormView, View
from .forms import NewUserForm
from .Scrapper.Scrapper import get_rss_feeds

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
