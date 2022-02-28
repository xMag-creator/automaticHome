from django.core.management.base import BaseCommand
from automation.models import Device, Sensor

SENSORS = ['Thermometer1', 'Thermometer1', 'Barometer', 'Humidity_meter']


class Command(BaseCommand):
    help = 'Add to database basic sensors'

    def handle(self, *args, **options):
        for sensor in SENSORS:
            Sensor.objects.create(name=sensor, value=0, status='Ready')
