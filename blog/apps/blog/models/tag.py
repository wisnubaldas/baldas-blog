"""Tag model for blog app."""

from django.db import models
from django.utils.text import slugify


class Tag(models.Model):
    """Blog post tag."""

    name = models.CharField("Nama Tag", max_length=80)
    slug = models.SlugField("Slug", unique=True)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tag"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
