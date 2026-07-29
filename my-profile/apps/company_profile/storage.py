"""DatabaseStorage implementation for persistent serverless file storage."""

import logging
import mimetypes
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible

logger = logging.getLogger(__name__)


@deconstructible
class DatabaseStorage(Storage):
    """Django Storage engine storing uploaded files directly into the database.
    Ensures persistent media storage across stateless Vercel Serverless Function instances.
    """

    def __init__(self, option=None):
        pass

    def _get_model(self):
        from apps.company_profile.models.stored_file import StoredFile
        return StoredFile

    def _open(self, name, mode="rb"):
        clean_name = name.lstrip("/")
        try:
            StoredFile = self._get_model()
            sf = StoredFile.objects.get(name=clean_name)
            return ContentFile(bytes(sf.content), name=clean_name)
        except Exception:
            # Fallback to reading from MEDIA_ROOT if present
            try:
                target_path = settings.MEDIA_ROOT / clean_name
                with open(target_path, "rb") as f:
                    return ContentFile(f.read(), name=clean_name)
            except Exception:
                raise FileNotFoundError(f"File '{clean_name}' not found.")

    def _save(self, name, content):
        clean_name = name.lstrip("/")

        try:
            content.seek(0)
            file_bytes = content.read()
        except Exception:
            file_bytes = b""

        if isinstance(file_bytes, str):
            file_bytes = file_bytes.encode("utf-8")
        elif not isinstance(file_bytes, (bytes, bytearray, memoryview)):
            file_bytes = bytes(file_bytes)
        else:
            file_bytes = bytes(file_bytes)

        mime_type, _ = mimetypes.guess_type(clean_name)
        mime_type = mime_type or "application/octet-stream"

        # 1. Try DB save
        try:
            StoredFile = self._get_model()
            StoredFile.objects.update_or_create(
                name=clean_name,
                defaults={
                    "content": file_bytes,
                    "content_type": mime_type,
                    "size": len(file_bytes),
                },
            )
        except Exception as e:
            logger.warning(f"DatabaseStorage DB write warning for '{clean_name}': {e}")

        # 2. Try disk save (local dev or /tmp)
        try:
            target_path = settings.MEDIA_ROOT / clean_name
            target_path.parent.mkdir(parents=True, exist_ok=True)
            with open(target_path, "wb") as f:
                f.write(file_bytes)
        except Exception:
            pass

        return clean_name

    def exists(self, name):
        clean_name = name.lstrip("/")
        try:
            StoredFile = self._get_model()
            if StoredFile.objects.filter(name=clean_name).exists():
                return True
        except Exception:
            pass
        return (settings.MEDIA_ROOT / clean_name).exists()

    def url(self, name):
        clean_name = name.lstrip("/")
        media_url = getattr(settings, "MEDIA_URL", "/media/")
        if not media_url.endswith("/"):
            media_url += "/"
        return f"{media_url}{clean_name}"

    def size(self, name):
        clean_name = name.lstrip("/")
        try:
            StoredFile = self._get_model()
            sf = StoredFile.objects.get(name=clean_name)
            return sf.size or len(sf.content)
        except Exception:
            pass
        try:
            return (settings.MEDIA_ROOT / clean_name).stat().st_size
        except Exception:
            return 0

    def delete(self, name):
        clean_name = name.lstrip("/")
        try:
            StoredFile = self._get_model()
            StoredFile.objects.filter(name=clean_name).delete()
        except Exception:
            pass
        try:
            (settings.MEDIA_ROOT / clean_name).unlink(missing_ok=True)
        except Exception:
            pass
