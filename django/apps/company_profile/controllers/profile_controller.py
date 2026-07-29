"""Profile controller for company_profile app."""

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from apps.company_profile.models import Profile


def profile(request: HttpRequest) -> HttpResponse:
    """Profile / about section — redirects to home anchor."""
    from django.shortcuts import redirect
    return redirect("company_profile:home")
