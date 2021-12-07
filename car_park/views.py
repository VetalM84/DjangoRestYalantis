from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Driver, Vehicle


def home(request):
    drivers = Driver.objects.all()
    vehicles = Vehicle.objects.all()
    context = {'drivers': drivers, 'vehicles': vehicles}
    return render(request=request, template_name='car_park/home.html', context=context)
