from django.core.management.base import BaseCommand
from automation.models import Device


class Command(BaseCommand):
    help = 'Delete all devices from database'

    def handle(self, *args, **options):
        Device.objects.all().delete()
