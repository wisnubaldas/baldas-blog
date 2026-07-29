"""Profile, Skill, and SocialLink models for company_profile app."""

from django.db import models


class Profile(models.Model):
    """Singleton model for personal profile information."""

    full_name = models.CharField("Nama Lengkap", max_length=150)
    tagline = models.CharField("Tagline / Jabatan", max_length=200)
    bio = models.TextField("Bio Singkat")
    bio_detail = models.TextField("Bio Detail", blank=True)
    email = models.EmailField("Email")
    phone = models.CharField("Telepon", max_length=30, blank=True)
    location = models.CharField("Lokasi", max_length=100, blank=True)
    photo = models.ImageField("Foto Profil", upload_to="company_profile/uploads/profile/", blank=True)
    resume_file = models.FileField("File Resume", upload_to="company_profile/uploads/resume/", blank=True)

    is_active = models.BooleanField("Aktif", default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profil"

    def __str__(self):
        return self.full_name


class Skill(models.Model):
    """Technical or professional skill."""

    CATEGORY_CHOICES = [
        ("technical", "Technical"),
        ("soft", "Soft Skill"),
        ("language", "Bahasa"),
        ("tool", "Tools & Software"),
    ]

    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="skills", verbose_name="Profil"
    )
    name = models.CharField("Nama Skill", max_length=100)
    level = models.PositiveSmallIntegerField("Level (0-100)", default=80)
    category = models.CharField(
        "Kategori", max_length=20, choices=CATEGORY_CHOICES, default="technical"
    )
    icon = models.CharField("Icon Class / Emoji", max_length=100, blank=True)
    order = models.PositiveSmallIntegerField("Urutan", default=0)

    class Meta:
        verbose_name = "Keahlian"
        verbose_name_plural = "Keahlian"
        ordering = ["order", "name"]

    def __str__(self):
        return f"{self.name} ({self.level}%)"


class SocialLink(models.Model):
    """Social media or professional links."""

    PLATFORM_CHOICES = [
        ("github", "GitHub"),
        ("linkedin", "LinkedIn"),
        ("facebook", "Facebook"),
        ("instagram", "Instagram"),
        ("twitter", "Twitter / X"),
        ("youtube", "YouTube"),
        ("website", "Website"),
        ("other", "Lainnya"),
    ]

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="social_links",
        verbose_name="Profil",
    )
    platform = models.CharField("Platform", max_length=20, choices=PLATFORM_CHOICES)
    url = models.URLField("URL")
    icon_class = models.CharField("Icon CSS Class", max_length=100, blank=True)
    order = models.PositiveSmallIntegerField("Urutan", default=0)
    is_visible = models.BooleanField("Tampilkan", default=True)

    class Meta:
        verbose_name = "Link Sosial"
        verbose_name_plural = "Link Sosial"
        ordering = ["order"]

    def __str__(self):
        return f"{self.get_platform_display()} — {self.profile.full_name}"
