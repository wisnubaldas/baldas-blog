import os
from config.wsgi import application


def app(environ, start_response):
    """
    WSGI wrapper for Vercel Serverless Function deployment.
    Fixes Vercel internal rewrite path routing where Vercel prepends /api/index.py to PATH_INFO.
    """
    path_info = environ.get("PATH_INFO", "")

    # Clean up Vercel rewrite prefix if present
    if path_info.startswith("/api/index.py"):
        path_info = path_info[len("/api/index.py"):]
    elif path_info.startswith("/api/index"):
        path_info = path_info[len("/api/index"):]

    if not path_info:
        path_info = "/"

    environ["PATH_INFO"] = path_info
    environ["SCRIPT_NAME"] = ""

    return application(environ, start_response)
