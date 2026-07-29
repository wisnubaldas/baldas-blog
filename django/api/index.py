"""
Vercel Serverless Entry Point for Django.
Adds project root to sys.path, ensures static files are collected for WhiteNoise, and exports WSGI app.
"""

import os
import sys
from pathlib import Path

# Add project root directory to sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

# Ensure collectstatic is run so WhiteNoise always has staticfiles ready
staticfiles_dir = BASE_DIR / "staticfiles"
if not staticfiles_dir.exists() or not (staticfiles_dir / "company_profile").exists():
    from django.core.management import call_command
    try:
        call_command("collectstatic", "--noinput", verbosity=0)
    except Exception as e:
        print("Build-time collectstatic notice:", e)

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
app = application
