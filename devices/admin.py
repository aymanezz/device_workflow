from django.contrib import admin
from .models import Device, DeviceLog


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
list_display = ('serial_number', 'customer_name', 'project_type', 'status', 'warranty', 'assigned_to', 'created_at')
list_filter = ('status', 'project_type', 'warranty')
search_fields = ('serial_number', 'customer_name')


@admin.register(DeviceLog)
class DeviceLogAdmin(admin.ModelAdmin):
list_display = ('device', 'previous_status', 'new_status', 'user', 'timestamp')
readonly_fields = ('timestamp',)