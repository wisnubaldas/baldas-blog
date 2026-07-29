"""
Django settings for blog project (blog.wisnubaldas.net).
"""

from pathlib import Path
from decouple import config, Csv
import dj_database_url
import sys

# ─── Base Paths ────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent

# ─── Security ──────────────────────────────────────────────────────────────────
SECRET_KEY = config("SECRET_KEY", default="django-insecure-blog-key-change-in-production")
DEBUG = config("DEBUG", default=True, cast=bool)
ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS",
    default="localhost,127.0.0.1,blog.wisnubaldas.net,.vercel.app",
    cast=Csv(),
)

CSRF_TRUSTED_ORIGINS = config(
    "CSRF_TRUSTED_ORIGINS",
    default="http://localhost:8001,http://127.0.0.1:8001,https://blog.wisnubaldas.net,https://*.vercel.app",
    cast=Csv(),
)

MAIN_PROFILE_URL = config("MAIN_PROFILE_URL", default="https://wisnubaldas.net")

# Auto-add Vercel deployment preview host if present
VERCEL_URL = config("VERCEL_URL", default="")
if VERCEL_URL and VERCEL_URL not in ALLOWED_HOSTS:
    ALLOWED_HOSTS.append(VERCEL_URL)
    origin = f"https://{VERCEL_URL}"
    if origin not in CSRF_TRUSTED_ORIGINS:
        CSRF_TRUSTED_ORIGINS.append(origin)

# ─── Application Definition ────────────────────────────────────────────────────
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third-party
    "django_ckeditor_5",
    "django_htmx",
    # Local app
    "apps.blog.apps.BlogConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "config.context_processors.site_urls",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# ─── Database ──────────────────────────────────────────────────────────────────
# Dynamic selection:
# - Production (DEBUG=False): Uses PostgreSQL via DATABASE_URL
# - Local Dev (DEBUG=True): Uses SQLite (db.sqlite3) by default, or PostgreSQL if USE_POSTGRES=True
_database_url = config("DATABASE_URL", default="")
_is_collectstatic = "collectstatic" in sys.argv
_use_postgres = config("USE_POSTGRES", default=not DEBUG, cast=bool)

_has_psycopg = False
if _database_url and _use_postgres and not _is_collectstatic:
    try:
        import psycopg2  # noqa: F401
        _has_psycopg = True
    except Exception:
        try:
            import psycopg  # noqa: F401
            _has_psycopg = True
        except Exception:
            _has_psycopg = False

if _database_url and _use_postgres and not _is_collectstatic and _has_psycopg:
    DATABASES = {
        "default": dj_database_url.parse(
            _database_url,
            conn_max_age=600,
            conn_health_checks=True,
        )
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR.parent / "db.sqlite3",
        }
    }

# ─── Password Validation ────────────────────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ─── Internationalization ───────────────────────────────────────────────────────
LANGUAGE_CODE = "id"
TIME_ZONE = "Asia/Jakarta"
USE_I18N = True
USE_TZ = True

# ─── Static Files ───────────────────────────────────────────────────────────────
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

if not DEBUG:
    STORAGES = {
        "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
        },
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
    }

# ─── Media Files ────────────────────────────────────────────────────────────────
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ─── CKEditor 5 ─────────────────────────────────────────────────────────────────
CKEDITOR_5_CONFIGS = {
    "default": {
        "toolbar": {
            "items": [
                "heading", "|",
                "bold", "italic", "underline", "strikethrough", "|",
                "bulletedList", "numberedList", "blockQuote", "|",
                "link", "insertImage", "insertTable", "|",
                "undo", "redo",
            ],
            "shouldNotGroupWhenFull": True,
        },
        "image": {
            "toolbar": ["imageTextAlternative", "|", "imageStyle:full", "imageStyle:side"],
        },
        "table": {
            "contentToolbar": ["tableColumn", "tableRow", "mergeTableCells"],
        },
        "height": "400px",
        "width": "100%",
        "language": "id",
    },
}

CKEDITOR_5_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
CKEDITOR_5_UPLOAD_FILE_TYPES = ["jpeg", "pdf", "png", "svg", "gif", "webp"]

# ─── Default Primary Key ────────────────────────────────────────────────────────
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ─── Security Headers (Production) ─────────────────────────────────────────────
# Trust Vercel edge reverse proxy HTTPS header
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

if not DEBUG:
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = "DENY"
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
