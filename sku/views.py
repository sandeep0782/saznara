from django.shortcuts import render


def custom_404(request, exception):
    return render(request, "404.html", status=404)


def custom_500(request):
    return render(request, "500.html", status=500)


from django_ratelimit.exceptions import Ratelimited


def handler403(request, exception):

    if isinstance(exception, Ratelimited):
        return render(
            request,
            "errors/403.html",
            {
                "ratelimited": True,
            },
            status=429,
        )

    return render(
        request,
        "errors/403.html",
        {
            "ratelimited": False,
        },
        status=403,
    )
