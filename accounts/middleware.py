from django.shortcuts import redirect
from django.urls import reverse
from .models import Profile


class ProfileCompletionMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.user.is_authenticated:

            try:
                profile = request.user.profile

                allowed_urls = [
                    reverse("edit-profile", kwargs={"id": profile.id}),
                    reverse("logout"),
                ]

                if (
                    not profile.is_profile_complete
                    and request.path not in allowed_urls
                    and not request.path.startswith("/media/")
                    and not request.path.startswith("/static/")
                ):
                    return redirect("edit-profile", id=profile.id)

            except Profile.DoesNotExist:
                pass

        return self.get_response(request)