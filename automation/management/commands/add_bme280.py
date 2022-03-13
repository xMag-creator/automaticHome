from django.core.management.base import BaseCommand
from automation.models import Device
from automation.models import Sensor


class Command(BaseCommand):
    help = 'Add to database basic sensors'

    def handle(self, *args, **options):
        device = Device.objects.create(name='bme280',
                                       description='bme280: temperature, humity and pressure sensor',
                                       status='Ready')
        Sensor.objects.create(name='Temperature',
                              value=0,
                              device=device)
        Sensor.objects.create(name='Pressure',
                              value=0,
                              device=device)
        Sensor.objects.create(name='Humidity',
                              value=0,
                              device=device)
