from django.core.management.base import BaseCommand
from authapp.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        CustomUser.objects.create_superuser(
            'dgornin', 'dgornin@gmail.com', '200329', age=20
        )
