from rest_framework import serializers

from .models import Driver, Vehicle


class DriverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'first_name', 'last_name', 'created_at', 'updated_at']


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    driver_id = serializers.SlugRelatedField(
        queryset=Driver.objects.all(), slug_field='id')
    # make = serializers.CharField()
    # model = serializers.CharField()
    # plate_number = serializers.CharField()

    class Meta:
        model = Vehicle
        fields = ['id', 'driver_id', 'make', 'model', 'plate_number', 'created_at', 'updated_at']
