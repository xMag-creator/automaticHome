from .models import Device
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import DeviceSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows devices to be viewed or edited.
    """
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    # permission_classes = [permissions.IsAuthenticated]
