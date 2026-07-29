"""Root URL configuration for my-profile project (wisnubaldas.net)."""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    # Favicon — browser requests /favicon.ico
    path("favicon.ico", RedirectView.as_view(
        url="/static/company_profile/favicon.ico", permanent=True
    )),
    path("admin/", admin.site.urls),
    # Company Profile / Portofolio — root
    path("", include("apps.company_profile.urls", namespace="company_profile")),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Custom error handlers
handler404 = "apps.company_profile.controllers.home_controller.error_404"
handler500 = "apps.company_profile.controllers.home_controller.error_500"
