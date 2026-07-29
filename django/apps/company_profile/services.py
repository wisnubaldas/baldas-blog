"""Services for company_profile — optional business logic layer."""


def get_active_profile():
    """Return the active profile or None."""
    from apps.company_profile.models import Profile
    return Profile.objects.filter(is_active=True).first()
