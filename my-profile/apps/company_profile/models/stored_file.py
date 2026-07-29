"""StoredFile model for database-backed file storage."""

from django.db import models


class StoredFile(models.Model):
    """Stores uploaded media file content directly in the database for persistent storage on Vercel."""

    name = models.CharField("Nama Berkas", max_length=500, unique=True, db_index=True)
    content = models.BinaryField("Konten Berkas")
    content_type = models.CharField("MIME Type", max_length=100, default="application/octet-stream")
    size = models.PositiveIntegerField("Ukuran (Bytes)", default=0)
    created_at = models.DateTimeField("Dibuat", auto_now_add=True)
    updated_at = models.DateTimeField("Diperbarui", auto_now=True)

    class Meta:
        verbose_name = "Berkas Media"
        verbose_name_plural = "Berkas Media"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
