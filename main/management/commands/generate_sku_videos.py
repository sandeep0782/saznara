from django.core.management.base import BaseCommand

from main.models import SKUVideo


class Command(BaseCommand):
    help = "Generate pending SKU videos"

    def handle(self, *args, **options):
        videos = SKUVideo.objects.filter(status="pending").select_related("sku")

        count = videos.count()

        self.stdout.write(self.style.SUCCESS(f"Found {count} pending video(s)."))

        for video in videos:
            sku = video.sku

            self.stdout.write(f"Processing SKU: {sku.sku}")

            video.status = "generating"
            video.error_message = None

            video.save(
                update_fields=[
                    "status",
                    "error_message",
                    "updated_at",
                ]
            )

            # Gemini/Veo will be added here.

            self.stdout.write(
                self.style.SUCCESS(f"Video generation started for {sku.sku}")
            )
