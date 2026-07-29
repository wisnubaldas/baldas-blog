"""Contact URL routes for company_profile."""

from django.urls import path
from apps.company_profile.controllers.contact_controller import contact

urlpatterns = [
    path("send/", contact, name="contact_send"),
]
