"""Home controller for company_profile app."""

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from apps.company_profile.models import Profile, Experience, Project


def home(request: HttpRequest) -> HttpResponse:
    """Main one-page parallax landing view."""
    profile = Profile.objects.filter(is_active=True).first()
    experiences = (
        Experience.objects.filter(profile=profile).order_by("-start_date")
        if profile
        else []
    )
    projects = (
        Project.objects.filter(profile=profile, is_visible=True)
        .prefetch_related("tags", "images")
        .order_by("order", "-year")
        if profile
        else []
    )

    context = {
        "profile": profile,
        "experiences": experiences,
        "projects": projects,
    }
    return render(request, "company_profile/home.html", context)


def error_404(request: HttpRequest, exception=None) -> HttpResponse:
    """Custom 404 error page."""
    return render(request, "company_profile/404.html", status=404)


def error_500(request: HttpRequest) -> HttpResponse:
    """Custom 500 error page."""
    return render(request, "company_profile/500.html", status=500)
