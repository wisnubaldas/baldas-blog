"""Captcha utility for human verification and anti-spam protection in blog app."""

import random
from django.core.signing import TimestampSigner, BadSignature, SignatureExpired


def generate_captcha():
    """Generate a random math question and timestamped token.
    Returns (question_text, token).
    """
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    answer = num1 + num2
    question = f"Verifikasi Manusia: Berapa {num1} + {num2} = ?"

    signer = TimestampSigner()
    token = signer.sign(str(answer))
    return question, token


def verify_captcha(user_answer, token):
    """Verify user's answer against the signed timestamp token.
    Returns True if valid, False otherwise.
    """
    if not user_answer or not token:
        return False
    try:
        signer = TimestampSigner()
        expected_ans = signer.unsign(token, max_age=600)  # Token valid for 10 minutes
        return str(user_answer).strip() == str(expected_ans).strip()
    except (BadSignature, SignatureExpired, ValueError, AttributeError):
        return False
