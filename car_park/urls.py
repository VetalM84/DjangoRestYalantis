from django.urls import path, include

from rest_framework import routers

from .views import *

urlpatterns = [
    path('drivers/driver/', DriverList.as_view()),
    # path('drivers/driver/<driver_id>/', DriverList.as_view()),
    path('vehicles/vehicle/', VehicleList.as_view()),
    # path('vehicles/vehicle/<vehicle_id>/', VehicleList.as_view()),
]
