from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Device(models.Model):
PROJECT_CHOICES = [
('SLA', 'SLA'),
('Implementation', 'Under Implementation'),
('UnderWarranty', 'Under Warranty'),
('OutWarranty', 'Out of Warranty'),
('Market', 'Market Client'),
]


STATUS_CHOICES = [
('received', 'Received'),
('workshop', 'Workshop'),
('pre_inspection', 'Technical Pre-Inspection'),
('warranty_check', 'Warranty Check'),
('maintenance_internal', 'Maintenance - Internal'),
('maintenance_local', 'Maintenance - Local'),
('cost_approval', 'Cost Approval'),
('post_inspection', 'Technical Post-Inspection'),
('invoice', 'Invoice'),
('rma', 'RMA'),
('delivered', 'Delivered'),
]


serial_number = models.CharField(max_length=120, unique=True)
customer_name = models.CharField(max_length=200, blank=True)
project_type = models.CharField(max_length=30, choices=PROJECT_CHOICES, default='SLA')
status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='received')
warranty = models.BooleanField(default=False)
cost_approved = models.NullBooleanField()
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)


assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


def __str__(self):
return f"{self.serial_number} - {self.customer_name}"


class DeviceLog(models.Model):
device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='logs')
previous_status = models.CharField(max_length=50)
new_status = models.CharField(max_length=50)
user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
notes = models.TextField(blank=True)
timestamp = models.DateTimeField(auto_now_add=True)


def __str__(self):
return f"{self.device.serial_number} {self.previous_status} -> {self.new_status} @ {self.timestamp}"