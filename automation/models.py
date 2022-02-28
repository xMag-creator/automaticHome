from django.db import models


# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=128)


class Sensor(models.Model):
    name = models.CharField(max_length=128, unique=True)
    value = models.FloatField()
    device = models.ForeignKey(Device, on_delete=models.CASCADE)


class Actuator(models.Model):
    name = models.CharField(max_length=128, unique=True)
    value = models.FloatField()
    device = models.ForeignKey(Device, on_delete=models.CASCADE)