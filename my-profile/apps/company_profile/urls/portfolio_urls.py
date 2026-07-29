"""Portfolio URL routes for company_profile."""

from django.urls import path
from apps.company_profile.controllers.portfolio_controller import (
    list_projects,
    project_detail,
)

urlpatterns = [
    path("", list_projects, name="portfolio"),
    path("<slug:slug>/", project_detail, name="project_detail"),
]
