"""Root URL configuration for blog project (blog.wisnubaldas.net)."""

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.views.static import serve

urlpatterns = [
    # Favicon
    path("favicon.ico", RedirectView.as_view(
        url="/static/blog/favicon.ico", permanent=True
    )),
    path("admin/", admin.site.urls),
    path("ckeditor5/", include("django_ckeditor_5.urls")),
    # Serve media files directly via Django view (works in both local & Vercel production)
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    # Blog app — root of blog.wisnubaldas.net
    path("", include("apps.blog.urls", namespace="blog")),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
