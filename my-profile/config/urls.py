"""Root URL configuration for my-profile project (wisnubaldas.net)."""

from django.contrib import admin
from django.http import HttpResponse, Http404
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.views.static import serve

def serve_media(request, path):
    """Serve media files from DatabaseStorage first, with static filesystem fallback."""
    clean_path = path.lstrip("/")
    try:
        from apps.company_profile.models.stored_file import StoredFile
        sf = StoredFile.objects.filter(name=clean_path).first()
        if not sf:
            sf = StoredFile.objects.filter(name__endswith=clean_path).first()
        if sf:
            response = HttpResponse(bytes(sf.content), content_type=sf.content_type)
            response["Cache-Control"] = "public, max-age=31536000, immutable"
            return response
    except Exception:
        pass

    try:
        if (settings.MEDIA_ROOT / clean_path).exists():
            return serve(request, clean_path, document_root=settings.MEDIA_ROOT)
    except Exception:
        pass

    for static_dir in [
        settings.BASE_DIR / "apps" / "company_profile" / "static",
        settings.BASE_DIR / "static",
        settings.BASE_DIR / "staticfiles",
    ]:
        if (static_dir / clean_path).exists():
            return serve(request, clean_path, document_root=static_dir)

    raise Http404(f"Media file '{path}' not found.")


urlpatterns = [
    # Favicon — browser requests /favicon.ico
    path("favicon.ico", RedirectView.as_view(
        url="/static/company_profile/favicon.ico", permanent=True
    )),
    path("admin/", admin.site.urls),
    path("ckeditor5/", include("django_ckeditor_5.urls")),
    # Serve media files directly via DatabaseStorage + filesystem fallback
    re_path(r"^media/(?P<path>.*)$", serve_media),
    # Company Profile / Portofolio — root
    path("", include("apps.company_profile.urls", namespace="company_profile")),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Custom error handlers
handler404 = "apps.company_profile.controllers.home_controller.error_404"
handler500 = "apps.company_profile.controllers.home_controller.error_500"
