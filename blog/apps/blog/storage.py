"""DatabaseStorage implementation for persistent serverless file storage."""

import mimetypes
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible


@deconstructible
class DatabaseStorage(Storage):
    """Django Storage engine storing uploaded files directly into the database.
    Ensures persistent media storage across stateless Vercel Serverless Function instances.
    """

    def __init__(self, option=None):
        pass

    def _get_model(self):
        from apps.blog.models.stored_file import StoredFile
        return StoredFile

    def _open(self, name, mode="rb"):
        StoredFile = self._get_model()
        clean_name = name.lstrip("/")
        try:
            sf = StoredFile.objects.get(name=clean_name)
            return ContentFile(bytes(sf.content), name=clean_name)
        except StoredFile.DoesNotExist:
            raise FileNotFoundError(f"File '{clean_name}' not found in database storage.")

    def _save(self, name, content):
        StoredFile = self._get_model()
        clean_name = name.lstrip("/")

        content.seek(0)
        file_bytes = content.read()

        mime_type, _ = mimetypes.guess_type(clean_name)
        mime_type = mime_type or "application/octet-stream"

        StoredFile.objects.update_or_create(
            name=clean_name,
            defaults={
                "content": file_bytes,
                "content_type": mime_type,
                "size": len(file_bytes),
            },
        )

        # Cache on disk if MEDIA_ROOT is writable (for local dev speed)
        try:
            target_path = settings.MEDIA_ROOT / clean_name
            target_path.parent.mkdir(parents=True, exist_ok=True)
            with open(target_path, "wb") as f:
                f.write(file_bytes)
        except Exception:
            pass

        return clean_name

    def exists(self, name):
        StoredFile = self._get_model()
        clean_name = name.lstrip("/")
        return StoredFile.objects.filter(name=clean_name).exists()

    def url(self, name):
        clean_name = name.lstrip("/")
        media_url = getattr(settings, "MEDIA_URL", "/media/")
        if not media_url.endswith("/"):
            media_url += "/"
        return f"{media_url}{clean_name}"

    def size(self, name):
        StoredFile = self._get_model()
        clean_name = name.lstrip("/")
        try:
            sf = StoredFile.objects.get(name=clean_name)
            return sf.size or len(sf.content)
        except StoredFile.DoesNotExist:
            return 0

    def delete(self, name):
        StoredFile = self._get_model()
        clean_name = name.lstrip("/")
        StoredFile.objects.filter(name=clean_name).delete()
