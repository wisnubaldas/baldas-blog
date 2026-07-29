"""Post controller for blog app."""

from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from apps.blog.models import Category, Post


def post_list(request: HttpRequest) -> HttpResponse:
    """Blog index — paginated list of published posts."""
    posts_qs = (
        Post.objects.published().select_related("category").prefetch_related("tags")
    )
    categories = Category.objects.all()
    recent_posts = posts_qs[:5]

    paginator = Paginator(posts_qs, 9)
    page_number = request.GET.get("page", 1)
    page = paginator.get_page(page_number)

    context = {
        "page": page,
        "categories": categories,
        "recent_posts": recent_posts,
    }

    if getattr(request, "htmx", False) or request.headers.get("HX-Request"):
        return render(request, "blog/partials/post_grid.html", context)
    return render(request, "blog/index.html", context)


def post_detail(request: HttpRequest, slug: str) -> HttpResponse:
    """Single article detail page."""
    post = get_object_or_404(Post.objects.published(), slug=slug)
    related = (
        Post.objects.published().filter(category=post.category).exclude(pk=post.pk)[:3]
    )
    return render(request, "blog/post_detail.html", {"post": post, "related": related})
