from django.contrib import admin

from .models import Vehicle, Driver


class DriverAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'created_at')
    list_display_links = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'driver_id', 'make', 'model', 'created_at')
    list_display_links = ('make', 'model')
    search_fields = ('make', 'model')


admin.site.register(Driver, DriverAdmin)
admin.site.register(Vehicle, VehicleAdmin)
