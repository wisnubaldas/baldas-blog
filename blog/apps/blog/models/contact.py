"""ContactMessage model for blog app."""

from django.db import models


class ContactMessage(models.Model):
    """Visitor contact form submission saved to DB in blog context."""

    STATUS_CHOICES = [
        ("new", "Baru"),
        ("read", "Dibaca"),
        ("replied", "Dibalas"),
        ("archived", "Diarsipkan"),
    ]

    name = models.CharField("Nama", max_length=150)
    email = models.EmailField("Email")
    subject = models.CharField("Subjek", max_length=200, blank=True)
    message = models.TextField("Pesan")
    status = models.CharField(
        "Status", max_length=20, choices=STATUS_CHOICES, default="new"
    )
    ip_address = models.GenericIPAddressField("IP Address", null=True, blank=True)
    created_at = models.DateTimeField("Dikirim pada", auto_now_add=True)

    class Meta:
        verbose_name = "Pesan Kontak Blog"
        verbose_name_plural = "Pesan Kontak Blog"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.subject or '(tanpa subjek)'}"
