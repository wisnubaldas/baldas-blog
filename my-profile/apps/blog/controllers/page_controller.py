"""Page controller for blog static pages (about, contact)."""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


from django.contrib import messages
from apps.blog.models import ContactMessage


def about(request: HttpRequest) -> HttpResponse:
    """About me page in blog context."""
    return render(request, "blog/about.html")


def contact(request: HttpRequest) -> HttpResponse:
    """Contact page in blog context."""
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        subject = request.POST.get("subject", "").strip()
        message_body = request.POST.get("message", "").strip()

        errors = {}
        if not name:
            errors["name"] = "Nama wajib diisi."
        if not email:
            errors["email"] = "Email wajib diisi."
        if not message_body:
            errors["message"] = "Pesan wajib diisi."

        if not errors:
            ip = request.META.get("HTTP_X_FORWARDED_FOR", "").split(",")[0].strip()
            ip = ip or request.META.get("REMOTE_ADDR")

            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message_body,
                ip_address=ip or None,
            )

            if getattr(request, "htmx", False) or request.headers.get("HX-Request"):
                return render(
                    request,
                    "blog/partials/contact_success.html",
                    {"name": name},
                )

            messages.success(request, "Pesan berhasil dikirim! Terima kasih.")
            return render(request, "blog/contact.html", {"name": name, "success": True})

        context = {
            "errors": errors,
            "form_data": {"name": name, "email": email, "subject": subject, "message": message_body},
        }
        if getattr(request, "htmx", False) or request.headers.get("HX-Request"):
            return render(request, "blog/partials/contact_form.html", context)
        return render(request, "blog/contact.html", context)

    return render(request, "blog/contact.html")
