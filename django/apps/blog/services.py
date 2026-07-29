"""Services for blog app — optional business logic layer."""


def get_recent_posts(limit=5):
    """Return N most recent published posts."""
    from apps.blog.models import Post
    return Post.objects.published()[:limit]


def get_popular_categories():
    """Return categories with at least one published post."""
    from apps.blog.models import Category
    from django.db.models import Count
    return Category.objects.annotate(
        post_count=Count("posts")
    ).filter(post_count__gt=0).order_by("order", "name")
