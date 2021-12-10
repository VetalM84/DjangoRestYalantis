from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Driver, Vehicle
from .serializers import DriverSerializer, VehicleSerializer


class DriverList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = DriverSerializer

    def get_queryset(self):
        queryset = Driver.objects.all()
        date_gte = self.request.query_params.get('created_at__gte')
        date_lte = self.request.query_params.get('created_at__lte')
        if date_gte is not None:
            queryset = queryset.filter(created_at__gte=date_gte)
        elif date_lte is not None:
            queryset = queryset.filter(created_at__lte=date_lte)
        return queryset


class DriverDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class VehicleList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = VehicleSerializer

    def get_queryset(self):
        queryset = Vehicle.objects.all()
        with_drivers = self.request.query_params.get('with_drivers')
        if with_drivers == 'yes':
            queryset = queryset.filter(driver_id__isnull=False)
        elif with_drivers == 'no':
            queryset = queryset.filter(driver_id__isnull=True)
        return queryset


class VehicleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
