from django.conf import settings


def site_urls(request):
    """Provide global URLs like MAIN_PROFILE_URL to all templates."""
    return {
        "MAIN_PROFILE_URL": getattr(settings, "MAIN_PROFILE_URL", "https://wisnubaldas.net"),
    }
