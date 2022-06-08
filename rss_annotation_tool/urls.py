"""rss_annotation_tool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # By default, you can use positional parameters for path
    # eg: path("admin/", views.HomeView.as_view(), name="home")
    path("admin/", admin.site.urls),
    path("", views.HomeView.as_view(), name="home"),
    path(
        "users/auth/login",
        LoginView.as_view(template_name="auth_templates/login.html", next_page="/"),
        name="login",
    ),
    path(
        "users/auth/logout",
        LogoutView.as_view(next_page="/users/auth/login"),
        name="logout",
    ),
    path(
        "users/auth/register",
        views.RegisterUserView.as_view(),
        name="register_user",
    ),
    path(
        "users/bookmarks",
        views.BookmarksView.as_view(),
        name="bookmarks",
    ),
]
