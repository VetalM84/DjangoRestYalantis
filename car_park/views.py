from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from .models import Driver, Vehicle
from .serializers import DriverSerializer, VehicleSerializer


class DriverList(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class DriverDetail(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class VehicleList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehicleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
