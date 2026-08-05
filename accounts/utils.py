import requests
from django.conf import settings


def verify_turnstile(token, remote_ip=None):

    if not token:
        return False

    response = requests.post(
        "https://challenges.cloudflare.com/turnstile/v0/siteverify",
        data={
            "secret": settings.TURNSTILE_SECRET_KEY,
            "response": token,
            "remoteip": remote_ip,
        },
        timeout=10,
    )

    result = response.json()

    return result.get("success", False)
