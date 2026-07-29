"""URLs package for company_profile app.
Combines all sub-URL modules and exposes a single urlpatterns.
"""

from django.urls import path, include

app_name = "company_profile"

urlpatterns = [
    path("", include("apps.company_profile.urls.home_urls")),
    path("portfolio/", include("apps.company_profile.urls.portfolio_urls")),
    path("contact/", include("apps.company_profile.urls.contact_urls")),
]
