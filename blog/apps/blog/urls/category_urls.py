"""Category URL routes for blog."""

from django.urls import path
from apps.blog.controllers.category_controller import category_posts

urlpatterns = [
    path("<slug:slug>/", category_posts, name="category"),
]
