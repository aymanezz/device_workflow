from django.shortcuts import render, get_object_or_404, redirect
status = request.GET.get('status')
if status:
qs = qs.filter(status=status)
return render(request, 'devices/device_list.html', {'devices': qs})


@login_required
def device_create(request):
if request.method == 'POST':
form = DeviceForm(request.POST)
if form.is_valid():
device = form.save()
DeviceLog.objects.create(device=device, previous_status='', new_status=device.status, user=request.user, notes='Created')
return redirect('devices:device_detail', pk=device.pk)
else:
form = DeviceForm()
return render(request, 'devices/device_form.html', {'form': form})


@login_required
def device_detail(request, pk):
device = get_object_or_404(Device, pk=pk)
return render(request, 'devices/device_detail.html', {'device': device})


@login_required
def device_action(request, pk):
# central place to apply workflow transitions
device = get_object_or_404(Device, pk=pk)
action = request.POST.get('action')
note = request.POST.get('note', '')
prev = device.status


# define simple transitions; expand as needed
if action == 'to_pre_inspection':
device.status = 'pre_inspection'
elif action == 'to_warranty_check':
device.status = 'warranty_check'
elif action == 'warranty_yes':
device.status = 'rma'
device.warranty = True
elif action == 'warranty_no':
device.status = 'maintenance_internal'
device.warranty = False
elif action == 'maintenance_local':
device.status = 'maintenance_local'
elif action == 'to_cost_approval':
device.status = 'cost_approval'
elif action == 'cost_approve':
device.status = 'post_inspection'
device.cost_approved = True
elif action == 'cost_reject':
device.status = 'delivered'
device.cost_approved = False
elif action == 'post_inspection_done':
device.status = 'invoice'
elif action == 'invoice_done':
device.status = 'delivered'
elif action == 'deliver':
device.status = 'delivered'


device.save()
DeviceLog.objects.create(device=device, previous_status=prev, new_status=device.status, user=request.user, notes=note)
return redirect('devices:device_detail', pk=device.pk)