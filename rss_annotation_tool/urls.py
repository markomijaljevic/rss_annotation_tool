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

urlpatterns = [
    # By default, you can use positional parameters for path
    # eg: path("admin/", views.HomeView.as_view(), name="home")
    path(route="admin/", view=admin.site.urls),
    path(route="", view=views.HomeView.as_view(), name="home"),
    path(
        route="users/auth/login",
        view=views.LoginUserView.as_view(template_name="auth_templates/login.html"),
        name="login",
    ),
    path(
        route="users/auth/logout",
        view=views.LogoutUserView.as_view(),
        name="logout",
    ),
    path(
        route="users/auth/register",
        view=views.RegisterUserView.as_view(),
        name="register_user",
    ),
]
