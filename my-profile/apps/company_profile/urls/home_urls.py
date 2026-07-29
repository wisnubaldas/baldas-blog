"""Home URL routes for company_profile."""

from django.urls import path
from apps.company_profile.controllers.home_controller import home

urlpatterns = [
    path("", home, name="home"),
]
