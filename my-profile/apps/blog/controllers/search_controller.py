"""Search controller for blog app."""

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from apps.blog.models import Category, Post


def search(request: HttpRequest) -> HttpResponse:
    """Full-text search across post titles and excerpts."""
    query = request.GET.get("q", "").strip()
    posts_qs = Post.objects.none()

    if query:
        posts_qs = (
            Post.objects.published()
            .filter(
                Q(title__icontains=query)
                | Q(excerpt__icontains=query)
                | Q(body__icontains=query)
            )
            .select_related("category")
            .distinct()
        )

    paginator = Paginator(posts_qs, 9)
    page = paginator.get_page(request.GET.get("page", 1))

    context = {
        "query": query,
        "page": page,
        "categories": Category.objects.all(),
    }

    if getattr(request, "htmx", False) or request.headers.get("HX-Request"):
        return render(request, "blog/partials/search_results.html", context)
    return render(request, "blog/search.html", context)
