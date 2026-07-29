"""Search URL routes for blog."""

from django.urls import path
from apps.blog.controllers.search_controller import search

urlpatterns = [
    path("", search, name="search"),
]
