from django.core.management.base import BaseCommand

from main.models import VMS


class Command(BaseCommand):
    help = "Delete videos older than 45 days"

    def handle(self, *args, **kwargs):
        VMS.delete_old_videos()
        self.stdout.write(
            self.style.SUCCESS("Old videos deleted successfully")
        )