"""Experience model for company_profile app."""

from django.db import models
from apps.company_profile.models.profile import Profile


class Experience(models.Model):
    """Work experience or education entry."""

    TYPE_CHOICES = [
        ("work", "Pengalaman Kerja"),
        ("education", "Pendidikan"),
        ("certification", "Sertifikasi"),
        ("volunteer", "Volunteer"),
    ]

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="experiences",
        verbose_name="Profil",
    )
    type = models.CharField("Tipe", max_length=20, choices=TYPE_CHOICES, default="work")
    title = models.CharField("Jabatan / Gelar", max_length=200)
    organization = models.CharField("Perusahaan / Institusi", max_length=200)
    location = models.CharField("Lokasi", max_length=100, blank=True)
    start_date = models.DateField("Tanggal Mulai")
    end_date = models.DateField("Tanggal Selesai", null=True, blank=True)
    is_current = models.BooleanField("Masih Berlangsung", default=False)
    description = models.TextField("Deskripsi", blank=True)
    logo = models.ImageField(
        "Logo Organisasi", upload_to="experience/logos/", blank=True
    )
    order = models.PositiveSmallIntegerField("Urutan", default=0)

    class Meta:
        verbose_name = "Pengalaman"
        verbose_name_plural = "Pengalaman"
        ordering = ["-start_date"]

    def __str__(self):
        return f"{self.title} @ {self.organization}"

    @property
    def period(self):
        """Human-readable period string."""
        start = self.start_date.strftime("%b %Y")
        end = "Sekarang" if self.is_current else (
            self.end_date.strftime("%b %Y") if self.end_date else "—"
        )
        return f"{start} – {end}"
