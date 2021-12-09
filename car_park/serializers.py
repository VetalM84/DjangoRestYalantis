from rest_framework import serializers

from .models import Driver, Vehicle


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'first_name', 'last_name', 'created_at', 'updated_at']


class VehicleSerializer(serializers.ModelSerializer):
    # ReadOnlyField — это класс, возвращающий данные без изменения.
    # В этом случае он используется для возвращения поля username вместо стандартного id
    # driver_id = serializers.ReadOnlyField(source='driver_id.pk')

    # driver_id = serializers.SlugRelatedField(
    #     queryset=Driver.objects.all(), slug_field='id')
    # make = serializers.CharField()
    # model = serializers.CharField()
    # plate_number = serializers.CharField()

    class Meta:
        model = Vehicle
        fields = ['id', 'driver_id', 'make', 'model', 'plate_number', 'created_at', 'updated_at']
