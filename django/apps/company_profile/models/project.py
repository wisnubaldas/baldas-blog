"""Project and related models for company_profile app."""

from django.db import models
from apps.company_profile.models.profile import Profile


class ProjectTag(models.Model):
    """Technology/skill tag for a project."""

    name = models.CharField("Nama Tag", max_length=80)
    slug = models.SlugField(unique=True)
    color = models.CharField("Warna (hex)", max_length=10, default="#6c757d")

    class Meta:
        verbose_name = "Tag Proyek"
        verbose_name_plural = "Tag Proyek"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Project(models.Model):
    """Portfolio project."""

    STATUS_CHOICES = [
        ("completed", "Selesai"),
        ("ongoing", "Berlangsung"),
        ("maintained", "Dipelihara"),
    ]

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="projects",
        verbose_name="Profil",
    )
    title = models.CharField("Judul Proyek", max_length=200)
    slug = models.SlugField("Slug", unique=True)
    client = models.CharField("Klien / Perusahaan", max_length=200, blank=True)
    short_description = models.CharField("Deskripsi Singkat", max_length=300)
    description = models.TextField("Deskripsi Lengkap", blank=True)
    cover_image = models.ImageField(
        "Gambar Cover", upload_to="projects/covers/", blank=True
    )
    tags = models.ManyToManyField(ProjectTag, blank=True, verbose_name="Tags")
    role = models.CharField("Peran dalam Proyek", max_length=200, blank=True)
    status = models.CharField(
        "Status", max_length=20, choices=STATUS_CHOICES, default="completed"
    )
    year = models.PositiveSmallIntegerField("Tahun", null=True, blank=True)
    url = models.URLField("URL Proyek", blank=True)
    is_featured = models.BooleanField("Featured", default=False)
    is_visible = models.BooleanField("Tampilkan", default=True)
    order = models.PositiveSmallIntegerField("Urutan", default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Proyek"
        verbose_name_plural = "Proyek"
        ordering = ["order", "-year"]

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    """Additional images/screenshots for a project."""

    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="images", verbose_name="Proyek"
    )
    image = models.ImageField("Gambar", upload_to="projects/gallery/")
    caption = models.CharField("Keterangan", max_length=200, blank=True)
    order = models.PositiveSmallIntegerField("Urutan", default=0)

    class Meta:
        verbose_name = "Gambar Proyek"
        verbose_name_plural = "Gambar Proyek"
        ordering = ["order"]

    def __str__(self):
        return f"{self.project.title} — Gambar {self.order}"
