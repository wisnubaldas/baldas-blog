"""Portfolio controller for company_profile app."""

from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from apps.company_profile.models import Project, Profile


def list_projects(request: HttpRequest) -> HttpResponse:
    """HTMX-friendly project list partial or full page."""
    profile = Profile.objects.filter(is_active=True).first()
    tag_filter = request.GET.get("tag", "")

    projects = Project.objects.filter(is_visible=True).prefetch_related("tags", "images")
    if tag_filter:
        projects = projects.filter(tags__slug=tag_filter)

    context = {"projects": projects, "active_tag": tag_filter}

    if getattr(request, "htmx", False) or request.headers.get("HX-Request"):
        return render(request, "company_profile/partials/project_list.html", context)
    return render(request, "company_profile/portfolio.html", context)


def project_detail(request: HttpRequest, slug: str) -> HttpResponse:
    """Single project detail page."""
    profile = Profile.objects.filter(is_active=True).first()
    project = get_object_or_404(Project, slug=slug, is_visible=True)
    return render(request, "company_profile/portfolio_detail.html", {"project": project, "profile": profile})

