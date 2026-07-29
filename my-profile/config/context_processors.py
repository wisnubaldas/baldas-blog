from django.conf import settings


def site_urls(request):
    """Provide global URLs like BLOG_URL to all templates."""
    return {
        "BLOG_URL": getattr(settings, "BLOG_URL", "https://blog.wisnubaldas.net"),
    }
