"""
URLs package for blog app.
Combines all sub-URL modules and exposes a single urlpatterns.
"""

from django.urls import path, include

app_name = "blog"

urlpatterns = [
    path("category/", include("apps.blog.urls.category_urls")),
    path("search/", include("apps.blog.urls.search_urls")),
    path("pages/", include("apps.blog.urls.page_urls")),
    path("", include("apps.blog.urls.post_urls")),
]
