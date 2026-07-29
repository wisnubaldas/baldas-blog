"""Category model for blog app."""

from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    """Blog post category."""

    name = models.CharField("Nama Kategori", max_length=100)
    slug = models.SlugField("Slug", unique=True)
    description = models.TextField("Deskripsi", blank=True)
    color = models.CharField("Warna (hex)", max_length=10, default="#6c757d")
    order = models.PositiveSmallIntegerField("Urutan", default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategori"
        ordering = ["order", "name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
