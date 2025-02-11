"""
URL configuration for studyhub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include

from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("test/base/", TemplateView.as_view(template_name="base.html")),
    path("test/login/", TemplateView.as_view(template_name="login.html")),
    path("test/signup/", TemplateView.as_view(template_name="signup.html")),
    path("test/todo/", TemplateView.as_view(template_name="todo.html")),
    path("test/todo/form", TemplateView.as_view(template_name="todoform.html")),
    path("test/todo/detail", TemplateView.as_view(template_name="tododetail.html")),
    path("test/map/detail", TemplateView.as_view(template_name="search_detail.html")),
    path("test/map/result", TemplateView.as_view(template_name="search_result.html")),
    path("test/map", TemplateView.as_view(template_name="search.html")),
    path("", include("user.urls")),
    path("todo/", include("todo.urls")),
]
