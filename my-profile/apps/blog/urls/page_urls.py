"""Page (static) URL routes for blog."""

from django.urls import path
from apps.blog.controllers.page_controller import about, contact

urlpatterns = [
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
]
