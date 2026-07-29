"""Root URL configuration for blog-baldas project."""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    # Favicon — browser selalu request ke /favicon.ico
    path("favicon.ico", RedirectView.as_view(
        url="/static/company_profile/favicon.ico", permanent=True
    )),
    path("admin/", admin.site.urls),
    path("ckeditor5/", include("django_ckeditor_5.urls")),
    # Company Profile / Portofolio — root
    path("", include("apps.company_profile.urls", namespace="company_profile")),
    # Blog
    path("blog/", include("apps.blog.urls", namespace="blog")),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Custom error handlers
handler404 = "apps.company_profile.controllers.home_controller.error_404"
handler500 = "apps.company_profile.controllers.home_controller.error_500"
