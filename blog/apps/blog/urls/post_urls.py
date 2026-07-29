"""Post URL routes for blog."""

from django.urls import path
from apps.blog.controllers.post_controller import post_list, post_detail

urlpatterns = [
    path("", post_list, name="post_list"),
    path("<slug:slug>/", post_detail, name="post_detail"),
]
