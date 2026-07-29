"""Category controller for blog app."""

from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from apps.blog.models import Category, Post


def category_posts(request: HttpRequest, slug: str) -> HttpResponse:
    """List posts filtered by category."""
    category = get_object_or_404(Category, slug=slug)
    posts_qs = (
        Post.objects.published()
        .filter(category=category)
        .select_related("category")
        .prefetch_related("tags")
    )
    paginator = Paginator(posts_qs, 9)
    page = paginator.get_page(request.GET.get("page", 1))

    context = {
        "category": category,
        "page": page,
        "categories": Category.objects.all(),
    }

    if getattr(request, "htmx", False) or request.headers.get("HX-Request"):
        return render(request, "blog/partials/post_grid.html", context)
    return render(request, "blog/category.html", context)
