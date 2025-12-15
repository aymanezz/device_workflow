from django import forms
from .models import Device


class DeviceForm(forms.ModelForm):
class Meta:
model = Device
fields = ['serial_number', 'customer_name', 'project_type', 'warranty', 'assigned_to']