from django.urls import path

from .views import *

urlpatterns = [
    path('drivers/driver/', DriverList.as_view()),
    path('drivers/driver/<int:pk>/', DriverDetail.as_view()),
    path('vehicles/vehicle/', VehicleList.as_view()),
    path('vehicles/vehicle/<int:pk>/', VehicleDetail.as_view()),
    path('vehicles/set_driver/<int:pk>/', DriverInOutDetail.as_view()),
]
