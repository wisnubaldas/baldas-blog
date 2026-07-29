"""Contact controller for company_profile app."""

from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from apps.company_profile.models.contact import ContactMessage


def contact(request: HttpRequest) -> HttpResponse:
    """Handle contact form GET (partial render) and POST (save to DB)."""
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
            # Save to DB
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
                    "company_profile/partials/contact_success.html",
                    {"name": name},
                )

            messages.success(request, "Pesan berhasil dikirim! Terima kasih.")
            return redirect("company_profile:home")

        # Form has errors
        context = {
            "errors": errors,
            "form_data": {"name": name, "email": email, "subject": subject, "message": message_body},
        }
        if getattr(request, "htmx", False) or request.headers.get("HX-Request"):
            return render(request, "company_profile/partials/contact_form.html", context)
        return redirect("company_profile:home")

    return redirect("company_profile:home")
