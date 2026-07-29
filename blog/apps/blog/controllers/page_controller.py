"""Page controller for blog static pages (about, contact)."""

from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from apps.blog.models import ContactMessage
from apps.blog.utils.captcha import generate_captcha, verify_captcha


def about(request: HttpRequest) -> HttpResponse:
    """About me page in blog context."""
    return render(request, "blog/about.html")


def contact(request: HttpRequest) -> HttpResponse:
    """Contact page in blog context."""
    if request.method == "POST":
        honeypot = request.POST.get("website_url_check", "").strip()
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        subject = request.POST.get("subject", "").strip()
        message_body = request.POST.get("message", "").strip()
        captcha_answer = request.POST.get("captcha_answer", "").strip()
        captcha_token = request.POST.get("captcha_token", "").strip()

        errors = {}
        if not name:
            errors["name"] = "Nama wajib diisi."
        if not email:
            errors["email"] = "Email wajib diisi."
        if not message_body:
            errors["message"] = "Pesan wajib diisi."

        is_valid_captcha, captcha_msg = verify_captcha(
            request, captcha_answer, captcha_token, honeypot_value=honeypot
        )
        if not is_valid_captcha:
            errors["captcha"] = captcha_msg

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
            captcha_question, new_token = generate_captcha()
            return render(
                request,
                "blog/contact.html",
                {
                    "name": name,
                    "success": True,
                    "captcha_question": captcha_question,
                    "captcha_token": new_token,
                },
            )

        # Form has errors: generate a fresh captcha question for retry
        captcha_question, new_captcha_token = generate_captcha()
        context = {
            "errors": errors,
            "form_data": {
                "name": name,
                "email": email,
                "subject": subject,
                "message": message_body,
            },
            "captcha_question": captcha_question,
            "captcha_token": new_captcha_token,
        }
        if getattr(request, "htmx", False) or request.headers.get("HX-Request"):
            return render(request, "blog/partials/contact_form.html", context)
        return render(request, "blog/contact.html", context)

    captcha_question, captcha_token = generate_captcha()
    return render(
        request,
        "blog/contact.html",
        {
            "captcha_question": captcha_question,
            "captcha_token": captcha_token,
        },
    )
