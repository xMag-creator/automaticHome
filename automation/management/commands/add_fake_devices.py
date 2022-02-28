from django.core.management.base import BaseCommand
from automation.models import Device

DEVICES = ['window_1_bedroom', 'wash_machine', 'salon_light', 'furnace', 'weather_station']


class Command(BaseCommand):
    help = 'Add to database basic sensors'

    def handle(self, *args, **options):
        for name in DEVICES:
            Device.objects.create(name=name, description='', status='Ready')
