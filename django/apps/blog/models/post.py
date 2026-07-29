"""Post model for blog app."""

from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from apps.blog.models.category import Category
from apps.blog.models.tag import Tag


class PostManager(models.Manager):
    def published(self):
        return self.filter(status="published", published_at__lte=timezone.now())


class Post(models.Model):
    """Blog article / post."""

    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Dipublikasikan"),
    ]

    title = models.CharField("Judul", max_length=300)
    slug = models.SlugField("Slug", unique=True, max_length=320)
    excerpt = models.TextField("Ringkasan", max_length=500, blank=True)
    body = CKEditor5Field("Isi Artikel", config_name="default")
    cover_image = models.ImageField(
        "Gambar Cover", upload_to="blog/covers/%Y/%m/", blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="posts",
        verbose_name="Kategori",
    )
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="Tags")
    status = models.CharField(
        "Status", max_length=20, choices=STATUS_CHOICES, default="draft"
    )
    published_at = models.DateTimeField("Dipublikasikan pada", null=True, blank=True)
    created_at = models.DateTimeField("Dibuat", auto_now_add=True)
    updated_at = models.DateTimeField("Diperbarui", auto_now=True)

    objects = PostManager()

    class Meta:
        verbose_name = "Artikel"
        verbose_name_plural = "Artikel"
        ordering = ["-published_at", "-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        # Auto-set published_at when status changes to published
        if self.status == "published" and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    @property
    def reading_time(self):
        """Estimated reading time in minutes."""
        word_count = len(self.body.split()) if self.body else 0
        minutes = max(1, round(word_count / 200))
        return minutes
