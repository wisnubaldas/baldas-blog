"""Enterprise 5-layer Captcha utility for anti-scraping and human verification in blog app."""

import logging
import random
import time
from django.core.signing import TimestampSigner, BadSignature, SignatureExpired

logger = logging.getLogger(__name__)

NUM_WORDS = {
    1: "Satu", 2: "Dua", 3: "Tiga", 4: "Empat", 5: "Lima",
    6: "Enam", 7: "Tujuh", 8: "Delapan", 9: "Sembilan", 10: "Sepuluh"
}


def generate_captcha():
    """Generate a random math / word challenge with timestamped signature token."""
    challenge_type = random.choice(["num_add", "num_sub", "word_add", "word_sub"])

    if challenge_type == "num_add":
        num1, num2 = random.randint(1, 9), random.randint(1, 9)
        answer = num1 + num2
        question = f"Verifikasi Manusia: Berapa {num1} + {num2} = ?"
    elif challenge_type == "num_sub":
        num1 = random.randint(5, 12)
        num2 = random.randint(1, num1)
        answer = num1 - num2
        question = f"Verifikasi Manusia: Berapa {num1} - {num2} = ?"
    elif challenge_type == "word_add":
        num1, num2 = random.randint(1, 5), random.randint(1, 5)
        answer = num1 + num2
        question = f"Verifikasi Manusia: Berapa hasil dari {NUM_WORDS[num1]} ditambah {NUM_WORDS[num2]}?"
    else:  # word_sub
        num1 = random.randint(4, 9)
        num2 = random.randint(1, num1 - 1)
        answer = num1 - num2
        question = f"Verifikasi Manusia: Berapa hasil dari {NUM_WORDS[num1]} dikurangi {NUM_WORDS[num2]}?"

    created_at = time.time()
    payload = f"{answer}:{created_at}"

    signer = TimestampSigner()
    token = signer.sign(payload)
    return question, token


def verify_captcha(request, user_answer, token, honeypot_value=None):
    """Verify user's answer against the signed timestamp token.
    Checks:
    1. Honeypot check
    2. Token signature & age (max 10 mins)
    3. Time-delta check (min 2 seconds elapsed since page load to prevent instant bot POST)
    4. IP rate limiting (max 3 submits / 5 mins)

    Returns (is_valid, error_message).
    """
    # 1. Honeypot check
    if honeypot_value:
        logger.warning("Spam bot trapped by honeypot field.")
        return False, "Aktivitas terdeteksi sebagai spam otomatis."

    if not user_answer or not token:
        return False, "Jawaban verifikasi (CAPTCHA) wajib diisi."

    # 2. Token unsign
    try:
        signer = TimestampSigner()
        payload = signer.unsign(token, max_age=600)  # max 10 minutes
        parts = payload.split(":")
        expected_ans = parts[0]
        created_at = float(parts[1]) if len(parts) > 1 else 0
    except (BadSignature, SignatureExpired, ValueError, IndexError, AttributeError):
        return False, "Token verifikasi (CAPTCHA) kedaluwarsa atau tidak valid. Silakan coba lagi."

    # 3. Minimum time-delta check (prevent instant bot POST < 2.0s)
    elapsed = time.time() - created_at
    if created_at > 0 and elapsed < 2.0:
        logger.warning(f"Submission too fast ({elapsed:.2f}s). Likely bot.")
        return False, "Pengiriman terlalu cepat. Mohon tunggu sejenak dan coba lagi."

    # 4. Answer verification
    if str(user_answer).strip() != expected_ans.strip():
        return False, "Jawaban verifikasi manusia (CAPTCHA) salah. Silakan coba lagi."

    # 5. IP Rate limiting
    ip = request.META.get("HTTP_X_FORWARDED_FOR", "").split(",")[0].strip()
    ip = ip or request.META.get("REMOTE_ADDR") or "unknown"

    session_key = f"contact_submissions_{ip}"
    now = time.time()
    history = request.session.get(session_key, [])
    # keep submissions from last 300 seconds (5 minutes)
    recent = [t for t in history if now - t < 300]
    if len(recent) >= 3:
        return False, "Anda telah mengirim terlalu banyak pesan. Silakan tunggu 5 menit sebelum mencoba kembali."

    recent.append(now)
    request.session[session_key] = recent

    return True, None
