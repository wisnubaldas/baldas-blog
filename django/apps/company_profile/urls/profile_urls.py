"""Profile URL routes for company_profile."""

from django.urls import path
from apps.company_profile.controllers.profile_controller import profile

urlpatterns = [
    path("", profile, name="profile"),
]
