from django.urls import path, include
# from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

from .views import *

urlpatterns = [
    path('drivers/driver/', DriverList.as_view()),
    path('drivers/driver/<int:pk>/', DriverDetail.as_view()),
    path('vehicles/vehicle/', VehicleList.as_view()),
    path('vehicles/vehicle/<int:pk>/', VehicleDetail.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
