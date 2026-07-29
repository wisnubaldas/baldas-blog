"""Page controller for blog static pages (about, contact)."""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def about(request: HttpRequest) -> HttpResponse:
    """About me page in blog context."""
    return render(request, "blog/about.html")


def contact(request: HttpRequest) -> HttpResponse:
    """Contact page in blog context."""
    return render(request, "blog/contact.html")
